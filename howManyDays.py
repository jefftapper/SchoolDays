from datetime import timedelta, date
import json

def howManySchoolDaysRemain(theDate, dateList):
    return dateList[theDate.strftime("%x")]


def getStartDay():
    startDate = date(2016, 9, 8)
    return startDate


def getEndDay():
    endDate = date(2017, 6, 28)
    return endDate

def howManyLeft():
    with open('SchoolDataNYC20162017.json') as data:
        dateList = json.load(data)
    today = date.today()
    return howManySchoolDaysRemain(today, dateList)

def whenIsLastDay():
    return getEndDay()


print howManyLeft()
