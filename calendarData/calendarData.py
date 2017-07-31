# Authorize server-to-server interactions from Google Compute Engine.
import sys
import time
from oauth2client.contrib import gce
import httplib2
import traceback
from apiclient import discovery
from apiclient.discovery import build
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuick import *
from PyQt5.QtQml import *           #import qtqml engine

import datetime
import dateutil.parser

class MyCalendarData(QThread):

    #qt signal for the calendar data
    calendarChanged = pyqtSignal()

    def __init__(self, parent = None):
        super(MyCalendarData, self).__init__(parent)
        #self.timer = QTimer(self)
        #changes calendar every 10 minutes, could make this a dynamic variable
    #    self.timer.setInterval(1000000) #2000000
        #run the emitNow function every second to emit the signal for realtime
    #    self.timer.timeout.connect(self.emitNow)
    #    self.timer.start()


    @pyqtSlot()
    def run(self):
        while True:
            #changes calendar every 10 minutes, could make this a dynamic variable
            time.sleep(.5)
            self.calendarChanged.emit()  #emit calendar signal
            print "emit greeting signal"
            time.sleep(600)



    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Calendar API Python Quickstart'


    client_id = '1030590791912-r926h83equ95ncv9mot6s8r0dd48l6tt.apps.googleusercontent.com'
    client_secret = 'Djj25CyJ7-xkQEIev1xQXGER'

    # The scope URL for read/write access to a user's calendar data
    scope = 'https://www.googleapis.com/auth/calendar'

    flow = OAuth2WebServerFlow(client_id, client_secret, scope)

    @pyqtProperty('QVariant', notify=calendarChanged)
    def calRequest(self):
        storage = Storage('credentials.dat')
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

        # Create an httplib2.Http object to handle our HTTP requests, and authorize it
        # using the credentials.authorize() function.
        http = httplib2.Http()
        http = credentials.authorize(http)

        #disable SSL certs validation
        httplib2.Http(disable_ssl_certificate_validation=True)

        service = build('calendar', 'v3', http=http)
        try:
            now = datetime.datetime.now().isoformat() + 'Z'#.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
            #   primary calendar for user
            request = service.events().list(calendarId='primary', maxResults=5, orderBy="startTime",
                                    singleEvents=True, timeMin=now)
            # Get the next page.
            response = request.execute()
            # Accessing the response like a dict object with an 'items' key
            # returns a list of item objects (events).
            events = response.get('items', [])
            eventsList = []


            if not events:
                print "No upcoming events found"
            for event in events:
                eventsDict = {}
                 #The event object is a dict object with a 'summary' key.
                todayDay = datetime.datetime.now().day
                todayDate = datetime.datetime.now()
                tommorrowDay = datetime.datetime.now() + datetime.timedelta(days=1)
                startIsoDateTime = event["start"]["dateTime"]
                endIsoDateTime = event["end"]["dateTime"]
                #converts the iso date string into a python date object
                startDateTime = dateutil.parser.parse(startIsoDateTime)
                endDateTime = dateutil.parser.parse(endIsoDateTime)
                dayOfEvent =  startDateTime.strftime("%A")
                startTime = startDateTime.strftime("%-I:%M %p")
                endTime = endDateTime.strftime("%-I:%M %p")
                eventSummary = event.get('summary')


                if(todayDay == startDateTime.day):
                    dayOfEvent = "Today"
                elif(tommorrowDay.day == startDateTime.day):
                    dayOfEvent = "Tommorrow"

                #if startDateTime >= todayDay:
                print '\n\n'+event.get('summary')
                print dayOfEvent
                print startTime +" to "+ endTime+"\n"
                eventsDict["eventSummary"] = eventSummary
                eventsDict["eventDay"] = dayOfEvent
                eventsDict["startTime"] = startTime
                eventsDict["endTime"] = endTime
                eventsList.append(eventsDict)
            print eventsList
            return eventsList

        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get calendar event" % e

    print "Toye"
