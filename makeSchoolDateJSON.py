from datetime import timedelta, date
import json
from dateutil import parser


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
    if isDayOff(currentDate, vacationDays):
        return remainingDays
    else:
        return remainingDays + 1


def isDayOff(currentDate, vacationDays):
    if isWeekend(currentDate):
        return True
    if isVacationDay(currentDate.strftime("%x"), vacationDays):
        return True
    return False


def isWeekend(currentDate):
    if currentDate.weekday() > 4:
        return True
    else:
        return False


def isVacationDay(currentDate, vacationDays):
    if currentDate in vacationDays:
        return True
    else:
        return False


def dumpToJson(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
        # print json.dumps(data)


def makeJSON(filename):
    with open("NYC20162017SchoolDates.json", 'r') as data:
        obj = json.load(data)
    vacationDays = obj["vacationDays"]
    startDate = parser.parse(obj["startDate"])
    endDate = parser.parse(obj["endDate"])
    dateList = makeDateList(startDate, endDate, timedelta(days=-1), vacationDays)
    dumpToJson(dateList, filename)


makeJSON('SchoolDataNYC20162017.json')
