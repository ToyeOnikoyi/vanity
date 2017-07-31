import sys
from datetime import datetime
import random
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuick import *
from PyQt5.QtQml import *           #import qtqml engine



class DateTimeData(QThread):


    dateChanged = pyqtSignal()
    dayChanged = pyqtSignal()
    timeChanged = pyqtSignal()




    def __init__(self, parent = None):
        super(DateTimeData, self).__init__(parent)
        self.timeTimer = QTimer(self)
        self.timeTimer.setInterval(1000)
        #run the emitNow function every second to emit the signal for realtime
        self.timeTimer.timeout.connect(self.emitNow)
        self.timeTimer.start()
        #QThread.__init__(self)

#    self.emitNow()

    @pyqtSlot()
    def emitNow(self):
        self.dateChanged.emit()
        self.dayChanged.emit()
        self.timeChanged.emit()
        print "emit date time signal"

    @pyqtProperty(str, notify=dateChanged)
    def getDate(self):
        current_date_time = datetime.now() # gets the  current time object
        current_date = current_date_time.strftime("%b %-d, %Y") #gets day and year from local date
        print current_date
        return current_date

    @pyqtProperty(str, notify=dayChanged)
    def getDay(self):
        current_date_time = datetime.now() # gets the  current time object
        current_day = current_date_time.strftime("%A")   #gets the current day of the week
        print current_day
        return current_day

    @pyqtProperty(str, notify=timeChanged)
    def getTime(self):
        current_date_time = datetime.now() # gets the  current time object
        current_time = current_date_time.strftime("%-I:%M %p") #converts the time to string and formats for 12hr clock
        #time.sleep(2)
        print current_time
        return current_time


#    def run(self):
#        new_time = self.getTime()
#        self.dateTimeChanged.emit()
        #self.sleep(2)
