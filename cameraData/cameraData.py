import cv2
import numpy as np
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuick import *
from PyQt5.QtQml import *           #import qtqml engine

class MyCameraData(QThread):

    cameraChanged = pyqtSignal()

    def __init__(self, parent = None):
        super(MyCameraData, self).__init__(parent)


    @pyqtSlot()
    def run(self):

        self.cameraChanged.emit()
        print "emit Camera signal"

    @pyqtProperty(str, notify=cameraChanged)
    def cameraSource(self):
        #gets the webcam
        cam=cv2.VideoCapture(0)
        ret,img = cam.read()
        print "camera should be working"
        #while(True):
        return cam
