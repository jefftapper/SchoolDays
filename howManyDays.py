from datetime import date, datetime
import json


def howManySchoolDaysRemain(theDate, dateList):
    return dateList[theDate.strftime("%x")]


def getEndDay(dateList):
    dateArray = []
    for dates in dateList:
        dateArray.append(datetime.strptime(dates, "%m/%d/%y"))
    dateArray = sorted(dateArray)
    return dateArray[len(dateArray) - 1]


def howManyLeft():
    today = date.today()
    return numDaysRemaining(today)


def numDaysRemaining(theDate):
    dateList = getDateList()
    if theDate > getEndDay(dateList).date():
        return 0
    return howManySchoolDaysRemain(theDate, dateList)

def getDateList():
    with open('SchoolDataNYC20162017.json') as data:
        dates = json.load(data)
    return dates


def whenIsLastDay():
    return getEndDay(getDateList())


print howManyLeft()

print whenIsLastDay()

print numDaysRemaining(date(2017, 6, 29))