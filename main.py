
import sys
import threading
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuick import *
from PyQt5.QtQml import *           #import qtqml engine
from greeting.greeting import GreetingData
from dateTime.dateTime import DateTimeData
from weather.weather import WeatherData
from calendarData.calendarData import MyCalendarData
from cameraData.cameraData import MyCameraData
from houndData.hound import HoundThread
from houndData.hotword import HotWordThread


#obj = GreetingData()
#obj.emitNow()


# Main Function, run this to run app.
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)

    appEngine = QQmlApplicationEngine()
    context = appEngine.rootContext()


    greetingData = GreetingData()
    dateTimeData = DateTimeData()
    weatherData = WeatherData()
    calendarData = MyCalendarData()
    cameraData = MyCameraData()
    houndThread = HoundThread()
    hotWordThread = HotWordThread()

    greetingData.start()
    dateTimeData.start()
    weatherData.start()
    calendarData.start()
    cameraData.start()
    houndThread.start()
    hotWordThread.start()






    #set the context property for all python server data to qml
    context.setContextProperty('greetingData', greetingData)
    context.setContextProperty('dateTimeData', dateTimeData)
    context.setContextProperty('weatherData', weatherData)
    context.setContextProperty('calendarData', calendarData)
    context.setContextProperty('cameraData', cameraData)
    context.setContextProperty('houndThread', houndThread)
    context.setContextProperty('hotWordThread', hotWordThread)
    appEngine.load(QUrl('vanity2/qml/main.qml'))

    #win = appEngine.rootObjects()[0]

    #win.houndClicked.connect(houndData.getHound)

    #win.show()

    # Show the view
    #appEngine.show()


    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
