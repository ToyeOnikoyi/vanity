//import QtQuick 2.0
import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Window 2.2
import QtQml 2.2
import QtMultimedia 5.5
import QtQuick.Layouts 1.2
import QtQuick.Controls.Styles 1.4
//import greetings 1.0


Item{
    width: 470; height: 640
Label {
    id: greetingLabel
    anchors.verticalCenter: parent.verticalCenter
    anchors.horizontalCenter: parent.horizontalCenter
    text: greetingData.getGreeting
    horizontalAlignment: Text.AlignHCenter
    color: "white"
    //font: "times"
}


}
