from wit import Wit
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuick import *
from PyQt5.QtQml import *           #import qtqml engine

#client token
access_token = 'I5Z653LVKYIYH6QWOGM3XMPJAZZJYKRL'

class witWeatherData(QObject):

    client = Wit(access_token=access_token);

    def weather_action(entities):
        if 'weatherDay' in entities:
            weatherDay = str(entities['weatherDay'][0]['value'])
            print "day of the week: "+weatherDay
            if weatherDay == 'today':
                print "get todays weather"
            elif weatherDay == 'tomorrow':
                print "get tomorrows weather"
            elif  weatherDay == 'Monday':
                print "get mondays data"
        print "degrees"


    # My question
    resp = client.message('Is it going to be hot tomorrow?')

    entities = resp['entities']
    #json object of wit data
    print entities

    intent = resp['entities']['intent'][0]['value']

    if intent == 'get_weather':
        weather_action(entities)



    print "wit.AI response is: " +intent
