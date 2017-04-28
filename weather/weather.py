import requests
import random
import json
import forecastio
import traceback
from datetime import datetime
from PIL import Image
#import pytz
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuick import *
from PyQt5.QtQml import *


#########################################
                #CONSTANTS

weather_api_token = 'ded9b231aea341a33a894b37ff6cce75' # create account at https://darksky.net/dev/
weather_lang = 'en' # see https://darksky.net/dev/docs/forecast for full list of language parameters values
weather_unit = 'us' # see https://darksky.net/dev/docs/forecast for full list of unit parameters values
latitude = None # Set this if IP location lookup does not work for you (must be a string)
longitude = None # Set this if IP location lookup does not work for you (must be a string)

    # maps open weather icons to
# icon reading is not impacted by the 'lang' parameter
icon_lookup = {
    'clear-day': "assets/Sun.png",  # clear sky day
    'wind': "assets/Wind.png",   #wind
    'cloudy': "assets/Cloud.png",  # cloudy day
    'partly-cloudy-day': "assets/PartlySunny.png",  # partly cloudy day
    'rain': "assets/Rain.png",  # rain day
    'snow': "assets/Snow.png",  # snow day
    'snow-thin': "assets/Snow.png",  # sleet day
    'fog': "assets/Haze.png",  # fog day
    'clear-night': "assets/Moon.png",  # clear sky night
    'partly-cloudy-night': "assets/PartlyMoon.png",  # scattered clouds night
    'thunderstorm': "assets/Storm.png",  # thunderstorm
    'tornado': "assests/Tornado.png",    # tornado
    'hail': "assests/Hail.png"  # hail
}

class WeatherData(QObject):

    weatherChanged = pyqtSignal()

    def get_ip(self,):
        try:
            ip_url = "http://jsonip.com/"
            req = requests.get(ip_url)
            ip_json = json.loads(req.text)
            print ip_json
            return ip_json['ip']
        except Exception as e:
            traceback.print_exc()
            print "diddnt get ip"
            return "Error: %s. Cannot get ip." % e

    @pyqtSlot()
    def emitNow(self):
        self.weatherChanged.emit()
        print "emit weather data signal"

    @pyqtProperty(str, notify=weatherChanged)
    def getWeather(self):
        try:

            if latitude is None or longitude is None:
                # get my location
                location_req_url = "http://freegeoip.net/json/%s" % self.get_ip()
                r = requests.get(location_req_url)
                location_obj = json.loads(r.text)
                print location_obj

                lat = location_obj['latitude']
                lon = location_obj['longitude']

                #location2 = "%s, %s %" (location_obj['city'], location_obj['region_code'])

                # get the weather
                forecast = forecastio.load_forecast(weather_api_token, lat, lon)
            else:
                location2 = ''
                # get the weather
                forecast = forecastio.load_forecast(weather_api_token, lat, lon)


            degree_sign= u'\N{DEGREE SIGN}'
            self.temperature2 =  (str(int(forecast.currently().temperature)))
            self.currently2 = str(forecast.currently().summary)
            byHour = forecast.hourly()
            byDay = forecast.daily()
            self.forecast2 = byHour.summary

            self.tempMaxList = []
            self.tempMinList = []
            self.tempIconList = []
            #while numForcastDays <= 0:
            for dailyData in byDay.data:
                dailyTemperatureMax = str(int(dailyData.temperatureMax))
                dailyTemperatureMin = str(int(dailyData.temperatureMin))
                dailyIcon = dailyData.icon
                self.tempMaxList.append(dailyTemperatureMax)
                self.tempMinList.append(dailyTemperatureMin)
                self.tempIconList.append(dailyIcon)
            print self.tempMaxList
            print self.tempMinList
            print self.tempIconList




                #tempMaxList = []
                #self.dailyforecast2 = dailyData.summary
                #dailyTemperatureMax = dailyData.temperatureMax
                #tempMaxList.append(dailyTemperatureMax)
                #print dailyTemperatureMax
                #self.dailyTemperatureMin = dailyData.temperatureMin



            icon_id = forecast.currently().icon
            icon2 = None

            if icon_id in icon_lookup:
                icon2 = icon_lookup[icon_id]

            if icon2 is not None:
                icon = ''
                if icon != icon2:
                    icon = icon2
                #    image = Image.open(icon2)
                #    image = image.resize((100, 100), Image.ANTIALIAS)
                #    image = image.convert('RGB')
                #    photo = ImageTk.PhotoImage(image)

                #    self.iconLbl.config(image=photo)
                #    self.iconLbl.image = photo
            return self.temperature2, self.forecast2, self.tempMaxList, self.tempMinList

        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get weather." % e

    @pyqtProperty(str, notify=weatherChanged)
    def getCurrentTemp(self):
        a,b,c,d = self.getWeather
        currentTemp = a
        #print currentTemp
        return currentTemp

    @pyqtProperty(str, notify=weatherChanged)
    def getCurrentForcast(self):
        a,b,c,d = self.getWeather
        currentForcast = b
        #print currentForcast
        return currentForcast

    @pyqtProperty(str, notify=weatherChanged)
    def getTempMaxList(self):
        a,b,c,d = self.getWeather
        tempMaxList = c
        #print currentForcast
        return tempMaxList

    @pyqtProperty(str, notify=weatherChanged)
    def getTempMinList(self):
        a,b,c,d = self.getWeather
        tempMinList = d
        #print currentForcast
        return tempMinList



        #recalls this function after a minute
        #QtCore.QTimer.singleShot(9000, self.get_weather)
