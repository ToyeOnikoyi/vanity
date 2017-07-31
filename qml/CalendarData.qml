import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Window 2.2
import QtQml 2.2
import QtMultimedia 5.5
import QtQuick.Layouts 1.2
import QtQuick.Controls.Styles 1.4


Item{

width: 470; height: 640

//first event
Label{
    id:calEventDayOne
    text: calendarData.calRequest[0]["eventDay"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: 30
    color: "white"
}

Label{
    id:calEventOne
    text: calendarData.calRequest[0]["eventSummary"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventDayOne.y + 20
    color: "white"
}

Label{
    id:calEventTimeOne
    text: calendarData.calRequest[0]["startTime"]+ '  '+ calendarData.calRequest[0]["endTime"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventOne.y + 20
    color: "white"
}

//second event
Label{
    id:calEventDayTwo
    text: calendarData.calRequest[1]["eventDay"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventTimeOne.y + 30
    color: "white"
}

Label{
    id:calEventTwo
    text: calendarData.calRequest[1]["eventSummary"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventDayTwo.y + 20
    color: "white"
}

Label{
    id:calEventTimeTwo
    text: calendarData.calRequest[1]["startTime"]+ '  '+ calendarData.calRequest[1]["endTime"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventTwo.y + 20
    color: "white"
}

//third event
Label{
    id:calEventDayThree
    text: calendarData.calRequest[2]["eventDay"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventTimeTwo.y + 30
    color: "white"
}

Label{
    id:calEventThree
    text: calendarData.calRequest[2]["eventSummary"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventDayThree.y + 20
    color: "white"
}

Label{
    id:calEventTimeThree
    text: calendarData.calRequest[2]["startTime"]+ '  '+ calendarData.calRequest[4]["endTime"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventThree.y + 20
    color: "white"
}
/*
//fourth event
Label{
    id:calEventDayFour
    text: calendarData.calRequest[3]["eventDay"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventTimeThree.y + 30
    color: "white"
}

Label{
    id:calEventFour
    text: calendarData.calRequest[3]["eventSummary"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventDayFour.y + 10
    color: "white"
}

Label{
    id:calEventTimeFour
    text: calendarData.calRequest[3]["startTime"]+ '  '+ calendarData.calRequest[4]["endTime"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventDayFour.y + 10
    color: "white"
}

//fifth event
Label{
    id:calEventDayFive
    text: calendarData.calRequest[4]["eventDay"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventTimeFour.y + 30
    color: "white"
}

Label{
    id:calEventFive
    text: calendarData.calRequest[4]["eventSummary"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventDayFive.y + 10
    color: "white"
}

Label{
    id:calEventTimeFive
    text: calendarData.calRequest[4]["startTime"]+ '  '+ calendarData.calRequest[4]["endTime"]
    wrapMode: Text.WrapAnywhere     //Wraps text to the end of the view
    x: 0
    y: calEventFive.y + 10
    color: "white"
}
*/

}
