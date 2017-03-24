from datetime import date, datetime
import json


def howManySchoolDaysRemain(theDate, dateList):
    return dateList[theDate.strftime("%x")]


def getEndDay(dateList):
    print dateList

    dateArray = []
    for dates in dateList:
        dateArray.append(datetime.strptime(dates, "%m/%d/%y"))

    dateArray = sorted(dateArray)

    return dateArray[len(dateArray) - 1]


def howManyLeft():
    dateList = getDateList()
    today = date.today()
    return howManySchoolDaysRemain(today, dateList)


def getDateList():
    with open('SchoolDataNYC20162017.json') as data:
        dates = json.load(data)
    return dates


def whenIsLastDay():
    return getEndDay(getDateList())


# print howManyLeft()

print whenIsLastDay()
