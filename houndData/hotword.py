import snowboydecoder
import sys
import os
import signal
from PyQt5.QtCore import QThread, QObject
import hound

interrupted = False
speechRec = hound.HoundData()
TOP_DIR = os.path.dirname(os.path.abspath(__file__))
model = os.path.join(TOP_DIR, "resources/hey_vanity.pmdl")

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

#if len(sys.argv) == 1:
#    print("Error: need to specify model name")
#    print("Usage: python demo.py your.model")
#    sys.exit(-1)

class HotWordThread(QThread):

    def __init__(self, parent = None):
        super(HotWordThread, self).__init__(parent)


    def run(self):
        # capture SIGINT signal, e.g., Ctrl+C
        #signal.signal(signal.SIGINT, signal_handler)
        detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
        print('Listening... Press Ctrl+C to exit')

        # main loop
        detector.start(detected_callback=speechRec.getHound,#snowboydecoder.play_audio_file,
                       interrupt_check=interrupt_callback,
                       sleep_time=0.03)

        detector.terminate()
    def me(self):
        print('heyyyy')


#yo = HotWordThread()
#yo.run()
