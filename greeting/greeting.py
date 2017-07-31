import sys
import time
import random
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuick import *
from PyQt5.QtQml import *           #import qtqml engine


class GreetingData(QThread):


    greetingChanged = pyqtSignal()




    def __init__(self, parent = None):
        super(GreetingData, self).__init__(parent)
        self.timer = QTimer(self)
        #changes greeting every 20 minutes, could make this a dynamic variable
        self.timer.setInterval(2000000) #2000000
        #run the emitNow function every second to emit the signal for realtime
        self.timer.timeout.connect(self.emitNow)
        self.timer.start()

#    self.emitNow()

    @pyqtSlot()
    def emitNow(self):
        while True:
            time.sleep(.5)
            self.greetingChanged.emit()
            print "emit greeting signal"
            time.sleep(1200)

    @pyqtProperty(str, notify=greetingChanged)
    def getGreeting(self):
        morning_greeting = "Good Morning!"
        afternoon_greeting = "Good Afternoon!"
        evening_greeting = "Good Evening!"
        nite_greeting = "Good Nite!"
        greeting_by_time = "Default"
        #This if statement will say change the greeting by what time of day it is
        if datetime.hour < 12:
            greeting_by_time = morning_greeting
        elif datetime.hour >= 12 and datetime.hour <= 17:
            greeting_by_time = afternoon_greeting
        elif datetime.hour >= 17 and datetime.hour <= 21:
            greeting_by_time = evening_greeting
        elif datetime.hour >= 21 or datetime.hour <= 6:
            greeting_by_time = nite_greeting

        greeting_array = [greeting_by_time,"Hey Sexy","Hi Beautiful","looking Fresh","Dope outfit","You are so Cute"]

        return random.choice(greeting_array)
        print random.choice(greeting_array)



    #greetingValue = pyqtProperty('QString', fget=getGreeting, notify=greetingChanged)



#obj = GreetingData()
#obj.emitNow()
