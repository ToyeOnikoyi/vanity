
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuick import *
from PyQt5.QtQml import *           #import qtqml engine
from greeting.greeting import GreetingData
from dateTime.dateTime import DateTimeData
from weather.weather import WeatherData


#obj = GreetingData()
#obj.emitNow()


# Main Function, run this to run app.
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)
    # Create a label and set its properties
    #qmlRegisterType(GreetingData, 'greetings', 1, 0, 'GreetingData')
    appEngine = QQmlApplicationEngine()
    context = appEngine.rootContext()
    greetingData = GreetingData()
    dateTimeData = DateTimeData()
    weatherData = WeatherData()
    context.setContextProperty('greetingData', greetingData)
    context.setContextProperty('dateTimeData', dateTimeData)
    context.setContextProperty('weatherData', weatherData)
    appEngine.load(QUrl('vanity2/qml/main.qml'))
    #win = appEngine.rootObjects()

    #win.textUpdated.connect(showText)

    #win.show()

    # Show the view
    #appEngine.show()


    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
