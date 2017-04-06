import json

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

def readSchoolData(file):
    with open(file, 'r') as data:
        obj = json.load(data)
        return obj
