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
    ipChanged = pyqtSignal()


    def __init__(self, parent = None):
        super(WeatherData, self).__init__(parent)
        self.timer = QTimer(self)
        #updates weather every 1 hour, could make this a dynamic variable
        self.timer.setInterval(3600000)
        #run the emitNow function every second to emit the signal for realtime
        self.timer.timeout.connect(self.emitNow)
        self.timer.start()



    @pyqtProperty(str, notify=ipChanged)
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
        self.ipChanged.emit()
        print "emit weather data and ip signal"

    @pyqtProperty(str, notify=weatherChanged)
    def getWeather(self):
        try:

            if latitude is None or longitude is None:
                # get my location
                location_req_url = "http://freegeoip.net/json/%s" % self.get_ip()
                r = requests.get(location_req_url)
                location_obj = json.loads(r.text)
                #print location_obj

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
            self.maxMinTemp = {}
            self.maxMinTempList = []
            #while numForcastDays <= 0:
            for dailyData in byDay.data:
                dailyTemperatureMax = str(int(dailyData.temperatureMax)) #daily max temp
                dailyTemperatureMin = str(int(dailyData.temperatureMin))
                dailyDay = dailyData.time.strftime("%a") #day of the daily weather
                dailyIcon = dailyData.icon
                self.tempMaxList.append(dailyTemperatureMax)
                self.tempMinList.append(dailyTemperatureMin)
                self.tempIconList.append(dailyIcon)
                self.maxMinTemp = {
                    "maximum": dailyTemperatureMax,
                    "minimum": dailyTemperatureMin,
                    "img": dailyIcon,
                    "day": dailyDay
                }
                #append each maxMin dict to the corresponding list
                self.maxMinTempList.append(self.maxMinTemp)
            #print self.maxMinTempList
            #print self.tempMaxList
            #print self.tempMinList
            #print self.tempIconList





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
            return self.temperature2, self.forecast2, self.maxMinTempList

        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get weather." % e

    @pyqtProperty(str, notify=weatherChanged)
    def getCurrentTemp(self):
        a,b,c = self.getWeather
        currentTemp = a
        #print currentTemp
        return currentTemp

    @pyqtProperty(str, notify=weatherChanged)
    def getCurrentForcast(self):
        a,b,c = self.getWeather
        currentForcast = b
        #print currentForcast
        return currentForcast
    #convert python list to c++ array using QVariant. needed for qml to parse list
    @pyqtProperty("QVariant", notify=weatherChanged)
    def getMaxMinTempList(self):
        a,b,c = self.getWeather
        MaxMinTempList = c
        #print currentForcast
        return MaxMinTempList

    @pyqtProperty("QVariant", notify=weatherChanged)
    def getMaxMinIconList(self):
        a,b,c = self.getWeather
        MaxMinTempList = c
        #if MaxMinTempList["img"] == "clear-day":
        #    continue
        #elif MaxMinTempList["img"] == "clear-night":
        #    continue
        #elif MaxMinTempList["img"] == "rain":
        #    continue
        #elif MaxMinTempList["img"] == "snow":
    #        continue
    #    elif MaxMinTempList["img"] == "sleet":
    #        continue
    #    elif MaxMinTempList["img"] == "wind":
    #        continue
    #    elif MaxMinTempList["img"] == "fog":
    #        continue
    #    elif MaxMinTempList["img"] == "cloudy":
    #        continue
    #    elif MaxMinTempList["img"] == "partly-cloudy-day":
    #        continue
    #    elif MaxMinTempList["img"] == "partly-cloudy-night":
    #        continue
    #    elif MaxMinTempList["img"] == "hail":
    #        continue
    #    elif MaxMinTempList["img"] == "thunderstorm":
    #        continue
    #    elif MaxMinTempList["img"] == "tornado":
    #        continue

        return MaxMinTempList







        #recalls this function after a minute
        #QtCore.QTimer.singleShot(9000, self.get_weather)
