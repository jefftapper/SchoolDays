import json
from datetime import timedelta

from dateutil import parser

import SchoolDaysUtils

inputFileName = '../resources/data/NYC20172018SchoolDates.json'
outputFileName = '../resources/data/SchoolDataNYC20172018.json'
def makeVacationDay(day, vacationDays):
    vacationDays[day] = True


# returns array of dates
def makeDateList(start, end, delta, vacationDays):
    daysRemaining = 0
    returnArray = {}
    currentDate = end
    while currentDate >= start:
        returnArray[currentDate.strftime("%x")] = daysRemaining
        daysRemaining = getDaysRemaining(currentDate, daysRemaining, vacationDays)

        currentDate += delta
    return returnArray


def getDaysRemaining(currentDate, remainingDays, vacationDays):
    if SchoolDaysUtils.isDayOff(currentDate, vacationDays):
        return remainingDays
    else:
        return remainingDays + 1


def dumpToJson(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
        # print json.dumps(data)


def makeJSON(input):
    obj = SchoolDaysUtils.readSchoolData(input)
    vacationDays = obj["vacationDays"]
    startDate = parser.parse(obj["startDate"])
    endDate = parser.parse(obj["endDate"])
    dateList = makeDateList(startDate, endDate, timedelta(days=-1), vacationDays)
    #dateList = sorted(dateList)
    dumpToJson(dateList, outputFileName)


makeJSON(inputFileName)
