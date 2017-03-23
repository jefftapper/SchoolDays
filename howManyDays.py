from datetime import datetime, timedelta, date
import json;

def makeVacationDay(day,vacationDays):
    vacationDays[day] = True;

#returns array of dates
def makeDateList(start,end,delta,vacationDays):
    daysRemaining=0
    returnArray = {};
    currentDate = end;
    while currentDate>start:

        returnArray[currentDate]=daysRemaining;
        daysRemaining = getDaysRemaining(currentDate, daysRemaining,vacationDays);

        currentDate+=delta;
    return returnArray;

def getDaysRemaining(currentDate,remainingDays,vacationDays):
    if(isDayOff(currentDate,vacationDays)):
        return remainingDays
    else:
        return remainingDays+1;

def isDayOff(currentDate,vacationDays):
    if(isWeekend(currentDate)):
        return True;
    if(isVacationDay(currentDate,vacationDays)):
        return True;
    return False;

def isWeekend(currentDate):
    if(currentDate.weekday()>4):
        return True;
    else:
        return False;

def isVacationDay(currentDate,vacationDays):
    if(currentDate in vacationDays):
        return True;
    else:
        return False;

def howManySchoolDaysRemain(date,dateList):
    return dateList[date];

def getStartDay():
    startDate = date(2016, 9, 8)
    return startDate;

def getEndDay():
    endDate = date(2017, 6, 28)
    return  endDate;

def howManyLeft():
    vacationDays = makeVacationList();
    startDate = getStartDay()
    endDate = getEndDay()
    dateList = makeDateList(startDate, endDate, timedelta(days=-1),vacationDays);
    today = date.today();
    return howManySchoolDaysRemain(today,dateList);

def whenIsLastDay():
    return getEndDay()

def makeVacationList():
    vacationDays = {}
    makeVacationDay(date(2016,9,12),vacationDays);
    makeVacationDay(date(2016,10,3),vacationDays);
    makeVacationDay(date(2016,10,4),vacationDays);
    makeVacationDay(date(2016,10,10),vacationDays);
    makeVacationDay(date(2016,10,12),vacationDays);
    makeVacationDay(date(2016,11,8),vacationDays);
    makeVacationDay(date(2016,11,11),vacationDays);
    makeVacationDay(date(2016,11,24),vacationDays);
    makeVacationDay(date(2016,11,25),vacationDays);
    makeVacationDay(date(2016,12,26),vacationDays);
    makeVacationDay(date(2016,12,27),vacationDays);
    makeVacationDay(date(2016,12,28),vacationDays);
    makeVacationDay(date(2016,12,29),vacationDays);
    makeVacationDay(date(2016,12,30),vacationDays);
    makeVacationDay(date(2017,1,2),vacationDays);
    makeVacationDay(date(2017,1,16),vacationDays);
    makeVacationDay(date(2017,2,20),vacationDays);
    makeVacationDay(date(2017,2,21),vacationDays);
    makeVacationDay(date(2017,2,22),vacationDays);
    makeVacationDay(date(2017,2,23),vacationDays);
    makeVacationDay(date(2017,2,24),vacationDays);
    makeVacationDay(date(2017,4,10),vacationDays);
    makeVacationDay(date(2017,4,11),vacationDays);
    makeVacationDay(date(2017,4,12),vacationDays);
    makeVacationDay(date(2017,4,13),vacationDays);
    makeVacationDay(date(2017,4,14),vacationDays);
    makeVacationDay(date(2017,4,17),vacationDays);
    makeVacationDay(date(2017,4,18),vacationDays);
    makeVacationDay(date(2017,5,29),vacationDays);
    makeVacationDay(date(2017,6,8),vacationDays);
    makeVacationDay(date(2017,6,12), vacationDays);
    makeVacationDay(date(2017,6,26),vacationDays);
    return vacationDays;




#print howManyLeft();
#print today
#print(len(dateList))

#for k, v in sorted(dateList.items()):
#    print k,v
