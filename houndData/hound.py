import sys
import time
sys.path.append('\Users\Bah\Desktop\VanitySDK\houndify_py\houndify')
import houndify
import pyaudio
import wave
import speech_recognition as sr
from requests import Request, Session

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuick import *
from PyQt5.QtQml import *           #import qtqml engine


import houndify




class HoundData(QObject):
    get_response = 'Say "hey Vanity" then your vanity request'
    def __init__(self, parent = None):
        super(HoundData, self).__init__(parent)

    #    self.timer = QTimer(self)
        #changes greeting every 20 minutes, could make this a dynamic variable
    #    self.timer.setInterval(1000) #2000000
        #run the emitNow function every second to emit the signal for realtime
    #    self.timer.timeout.connect(self.emitNow)
    #    self.timer.start()

    #@pyqtSlot()
    #def emitNow(self):
    #    self.houndChanged.emit()
    #    print "emit houndify signal"


    def getHound(self):
        # obtain audio from the microphone
        r = sr.Recognizer()
        # sample rate and chunk size needed to match that of snowboys
        with sr.Microphone(sample_rate = 16000, chunk_size = 2048) as source:
            print("Say something!")
            audio = r.listen(source)


        clientId = "01GtytrXBLSLwHARibM1-w=="
        clientKey = "hWKkQISSaQyLMYeqPbDcbv6TbbBsZIyJ9ab0aSGEw031l4NEZxwbzVUgT-veJ1i5GtBfDT13GaYzAngF-ifnhQ=="
        userId = "test_user"
        requestInfo = {
          'ClientID': clientId,
          'UserID': userId,
          'Latitude': 41.823989,
          'Longitude': -71.412834,

        }

        client = houndify.TextHoundClient(clientId, clientKey, userId, requestInfo)

        # The request asked speech to text (STT)
        querySTT = r.recognize_houndify(audio, client_id=clientId, client_key=clientKey)
        print querySTT

        # The response from the query2
        response = client.query(str(querySTT))

        HoundData.get_response = str(response["AllResults"][0]['SpokenResponse'])
        command_intent = str(response["AllResults"][0]["CommandKind"])

        command_type = str(response["AllResults"][0]["Result"][0]["commandType"])
        command_action = str(response["AllResults"][0]["Result"][0]["action"])

        all_data = response["AllResults"]

        if command_intent == "WeatherCommand":
            print 'This is a weather command'


        if command_intent == "LocalSearchCommand":
            print 'This is a local search command'

        if command_intent == "CallNumberCommand":
            print 'This is a call number command'

        if command_intent == "UberCommand":
            print 'This is a weather command'

        if command_intent == "LyftCommand":
            print 'This is a Lyft command'

        if command_intent == "InformationCommand":
            print 'This is an Information command'

        if command_intent == "DeviceControlCommand":
            print 'This is a Device Control command'

        if command_intent == "GreetingsCommand":
            print 'This is a greetings command'

        if command_type == "LightCommand":
            if command_action == "turn_light_on":
                print 'This is a Lights command to turn it on'
            if command_action == "turn_light_off":
                print 'This is a Lights command to turn it off'


        if command_intent == "CameraRecordCommand":
            print 'This is a Camera Record command'

        if command_intent == "CameraZoomCommand":
            print 'This is a Camera Zoom command'

        if command_intent == "NewsCommand":
            print 'This is a News command'

        if command_intent == "YoutubeSearchCommand":
            print 'This is a Youtube Search command'

        if command_intent == "YoutubeUploadCommand":
            print 'This is a Youtube Upload command'

        if command_intent == "MapsCommand":
            print 'This is a Maps command'

        if command_intent == "InstagramCommand":
            print 'This is a Instagram command'

        if command_intent == "MakeupRecommendationCommand":
            print 'This is a Makeup Recommendation command'

        if command_intent == "SportsCommand":
            print 'This is a Sports command'

        if command_intent == "NutritionCommand":
            print 'This is a Nutrition command'





        print "response: %s" %HoundData.get_response
        print "command intent: %s" %command_intent
        print all_data
        return HoundData.get_response

    def getHoundResponse(self):
        #self.response = self.getHound()
        test = "toyeeeeeeeee!!"
        print "houndify response recieved!"
        print ("responses: "+HoundData.get_response)
        return HoundData.get_response

class HoundThread(QThread):

    houndChanged = pyqtSignal()

    def __init__(self, parent = None):
        super(HoundThread, self).__init__(parent)



    def run(self):
        while True:
            time.sleep(.5)
            self.houndChanged.emit()



    @pyqtProperty(str, notify=houndChanged)
    def getHoundResponse(self):
        #hounddata = HoundData()
        #houndGetResponse = hounddata.getHoundResponse()
        houndResponse = HoundData.get_response
        print("response sent digga and toye here")
        return houndResponse





#payload = {'key1':'what is the weather'}
#r = Request('GET',url='https://api.houndify.com/v1/',params=payload)
