import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Window 2.2
import QtQml 2.2
import QtMultimedia 5.5
import QtQuick.Layouts 1.2
import QtQuick.Controls.Styles 1.4


Item{
    width: 470; height: 640
    id: item

Label{
    id:currentTemp
    text: weatherData.getCurrentTemp
    anchors.right: item.right      //moves Temp to the end of the view
    //x: 450
    y: 0
    color: "white"
}

Label{
    id:currentForcast
    text: weatherData.getCurrentForcast
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 300
    y: currentTemp.y + 20
    color: "white"
}


ListModel {
    id: dailyWeather
    ListElement {
        name: weatherData.getTempMaxList[1]
        number: weatherData.getTempMinList[1]
    }
    ListElement {
        name: weatherData.getTempMaxList[1]
        number: weatherData.getTempMinList[1]
    }
    ListElement {
        name: weatherData.getTempMaxList[2]
        number: weatherData.getTempMinList[2]
    }
    ListElement {
        name: weatherData.getTempMaxList[3]
        number: weatherData.getTempMinList[3]
    }
    ListElement {
        name: weatherData.getTempMaxList[4]
        number: weatherData.getTempMinList[4]
    }
    ListElement {
        name: weatherData.getTempMaxList[5]
        number: weatherData.getTempMinList[5]
    }
    ListElement {
        name: weatherData.getTempMaxList[6]
        number: weatherData.getTempMinList[6]
    }
}

ListView {
    width: 180; height: 200
    y: 300

    model: dailyWeather
    delegate: Text {
        text: name + " " + number
        color: "white"
    }
}





}
