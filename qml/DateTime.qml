import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Window 2.2
import QtQml 2.2
import QtMultimedia 5.5
import QtQuick.Layouts 1.2
import QtQuick.Controls.Styles 1.4

Item{

width: 470; height: 640

Label {
    id: timeLabel
    //anchors.verticalCenter: parent.verticalCenter
    anchors.horizontalCenter: parent.horizontalCenter
    text: dateTimeData.getTime
    //horizontalAlignment: Text.AlignRight
//    x: dateLabel.x + 150
    y: 0
    color: "white"

}

Label {
    id: dateLabel
    //anchors.verticalCenter: parent.verticalCenter
    //anchors.horizontalCenter: parent.horizontalCenter
    text: dateTimeData.getDate
    //horizontalAlignment: Text.AlignRight
    x: dayLabel.x + 55
    y: 0
    color: "white"

}

Label {
    id: dayLabel
    //anchors.verticalCenter: parent.verticalCenter
    //anchors.horizontalCenter: parent.horizontalCenter
    text: dateTimeData.getDay
    //horizontalAlignment: Text.AlignRight
    x: 0
    y: 0
    color: "white"

}



}
