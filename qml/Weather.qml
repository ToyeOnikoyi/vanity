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

Label{
    id:dayOneTemp
    text: weatherData.getMaxMinTempList[0]["maximum"]+ "  "+weatherData.getMaxMinTempList[0]["minimum"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 360
    y: currentForcast.y + 20
    color: "white"
}

Label{
    id:dayTwoTemp
    text: weatherData.getMaxMinTempList[1]["maximum"]+ "  "+weatherData.getMaxMinTempList[1]["minimum"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 360
    y: dayOneTemp.y + 20
    color: "white"
}

Label{
    id:dayThreeTemp
    text: weatherData.getMaxMinTempList[2]["maximum"]+ "  "+weatherData.getMaxMinTempList[2]["minimum"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 360
    y: dayTwoTemp.y + 20
    color: "white"
}

Label{
    id:dayFourTemp
    text: weatherData.getMaxMinTempList[3]["maximum"]+ "  "+weatherData.getMaxMinTempList[3]["minimum"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 360
    y: dayThreeTemp.y + 20
    color: "white"
}

Label{
    id:dayFiveTemp
    text:weatherData.getMaxMinTempList[4]["maximum"]+ "  "+weatherData.getMaxMinTempList[4]["minimum"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 360
    y: dayFourTemp.y + 20
    color: "white"
}

Label{
    id:daySixTemp
    text:weatherData.getMaxMinTempList[5]["maximum"]+ "  "+weatherData.getMaxMinTempList[5]["minimum"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 360
    y: dayFiveTemp.y + 20
    color: "white"
}

Label{
    id:daySevenTemp
    text: weatherData.getMaxMinTempList[6]["maximum"]+ "  "+weatherData.getMaxMinTempList[6]["minimum"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 360
    y: daySixTemp.y + 20
    color: "white"
}

Label{
    id:dayOneDay
    text: weatherData.getMaxMinTempList[0]["day"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 300
    y: currentForcast.y + 20
    color: "white"
}

Label{
    id:dayTwoDay
    text: weatherData.getMaxMinTempList[1]["day"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 300
    y: dayOneDay.y + 20
    color: "white"
}

Label{
    id:dayThreeDay
    text: weatherData.getMaxMinTempList[2]["day"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 300
    y: dayTwoDay.y + 20
    color: "white"
}

Label{
    id:dayFourDay
    text: weatherData.getMaxMinTempList[3]["day"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 300
    y: dayThreeDay.y + 20
    color: "white"
}

Label{
    id:dayFiveDay
    text: weatherData.getMaxMinTempList[4]["day"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 300
    y: dayFourDay.y + 20
    color: "white"
}

Label{
    id:daySixDay
    text: weatherData.getMaxMinTempList[5]["day"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 300
    y: dayFiveDay.y + 20
    color: "white"
}

Label{
    id:daySevenDay
    text: weatherData.getMaxMinTempList[6]["day"]
    height: parent.height
    width: 170
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 300
    y: daySixDay.y + 20
    color: "white"
}








}
