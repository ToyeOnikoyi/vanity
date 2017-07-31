import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Window 2.2
import QtQml 2.2
import QtMultimedia 5.5
import QtQuick.Layouts 1.2
import QtQuick.Controls.Styles 1.4


Item{
    width: 470; height: 640

/*Rectangle{
    id: "houndButton"
    anchors.verticalCenter: parent.verticalCenter
    anchors.horizontalCenter: parent.horizontalCenter
    color: "white"
    x: 100
    y: 100
    width: 60
    height: 30
    signal houndClicked()
    MouseArea {
        anchors.fill: parent
        onClicked: {
            houndData.getHound()
           //parent.houndClicked()  // emit the parent's signal
        }
    }

}*/
/*Button {
    id: "houndButton"
    anchors.verticalCenter: parent.verticalCenter
    anchors.horizontalCenter: parent.horizontalCenter
}*/

Label {
    id: houndLabel
    y:550
    anchors.horizontalCenter: parent.horizontalCenter
    text: houndThread.getHoundResponse
    horizontalAlignment: Text.AlignHCenter
    color: "white"
    //font: "times"

}

}
