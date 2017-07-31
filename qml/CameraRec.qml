import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Window 2.2
import QtQml 2.2
import QtMultimedia 5.5
import QtQuick.Layouts 1.2
import QtQuick.Controls.Styles 1.4


Rectangle{

id: cameraUI
width: 470; height: 640
color: "black"


state: "PhotoCapture"

    states: [
        State {
            name: "PhotoCapture"
            StateChangeScript {
                script: {
                    camera.captureMode = Camera.CaptureStillImage
                    camera.start()
                }
            }
        }]

        Camera {
              id: camera
              captureMode: Camera.CaptureStillImage

              imageCapture {
                  onImageCaptured: {
                      photoPreview.source = preview
                      stillControls.previewAvailable = true
                      cameraUI.state = "PhotoPreview"
                  }
              }

              videoRecorder {
                   resolution: "640x480"
                   frameRate: 30
              }
          }
        //
        VideoOutput {
            source: camera
            fillMode: PreserveAspectCrop
            focus: visible
        }

}
