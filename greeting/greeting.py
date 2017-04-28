import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuick import *
from PyQt5.QtQml import *           #import qtqml engine


class GreetingData(QObject):


    greetingChanged = pyqtSignal()




    def __init__(self, parent = None):
        super(GreetingData, self).__init__(parent)

#    self.emitNow()

    @pyqtSlot()
    def emitNow(self):
        self.greetingChanged.emit()
        print "emit greeting signal"

    @pyqtProperty(str, notify=greetingChanged)
    def getGreeting(self):
        greeting_array = ["Hey Sexy","Hi Beautiful","looking Fresh","Dope outfit","You are so Cute"]
        return random.choice(greeting_array)
        print random.choice(greeting_array)



    #greetingValue = pyqtProperty('QString', fget=getGreeting, notify=greetingChanged)



#obj = GreetingData()
#obj.emitNow()
