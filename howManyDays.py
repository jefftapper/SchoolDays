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

    with open('schooldaydata.json') as data:
        dateList = json.load(data)
        print(dateList)
    today = date.today()
    return howManySchoolDaysRemain(today, dateList)

def whenIsLastDay():
    return getEndDay()

'''
'''
print howManyLeft()
# print today
# print(len(dateList))

# for k, v in sorted(dateList.items()):
#    print k,v
