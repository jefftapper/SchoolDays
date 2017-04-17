import json
from datetime import date, datetime

from dateutil import parser

import SchoolDaysUtils;

inputFileName = './resources/data/NYC20162017SchoolDates.json'
dateListFileName ='./resources/data/SchoolDataNYC20162017.json'

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
    with open(dateListFileName) as data:
        dates = json.load(data)
    return dates


def whenIsLastDay():
    return getEndDay(getDateList())

def isThereSchoolOnDay(date):
    obj = SchoolDaysUtils.readSchoolData(inputFileName)
    vacationDays = obj["vacationDays"]
    startDate = parser.parse(obj["startDate"])
    endDate = parser.parse(obj["endDate"])
    #dateTimeOfDate = datetime.combine(date,datetime.time.min)
    if  date < startDate.date():
        return False
    if date > endDate.date():
        return False
    if SchoolDaysUtils.isDayOff(date, vacationDays):
        return False
    else:
        return True


print isThereSchoolOnDay(date(2017, 4, 9))
print howManyLeft()

print whenIsLastDay()

print numDaysRemaining(date(2017, 6, 29))