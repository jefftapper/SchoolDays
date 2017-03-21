from datetime import datetime, timedelta, date
import json;


startDate = date(2016,9,8)

endDate = date(2017,6,28)

dateList = {};
vacationDays={};



def makeVacationDay(day):
    vacationDays[day] = True;

#returns array of dates
def makeDateList(start,end,delta):
    daysRemaining=0
    returnArray = {};
    currentDate = end;
    while currentDate>start:

        returnArray[currentDate]=daysRemaining;
        daysRemaining = getDaysRemaining(currentDate, daysRemaining);

        currentDate+=delta;
    return returnArray;

def getDaysRemaining(currentDate,remainingDays):
    if(isDayOff(currentDate)):
        return remainingDays
    else:
        return remainingDays+1;

def isDayOff(currentDate):
    if(isWeekend(currentDate)):
        return True;
    if(isVacationDay(currentDate)):
        return True;
    return False;

def isWeekend(currentDate):
    if(currentDate.weekday()>4):
        return True;
    else:
        return False;

def isVacationDay(currentDate):
    if(currentDate in vacationDays):
        return True;
    else:
        return False;

def howManySchoolDaysRemain(date):
    return dateList[date];


makeVacationDay(date(2016,9,12));
makeVacationDay(date(2016,10,3));
makeVacationDay(date(2016,10,4));
makeVacationDay(date(2016,10,10));
makeVacationDay(date(2016,10,12));
makeVacationDay(date(2016,11,8));
makeVacationDay(date(2016,11,11));
makeVacationDay(date(2016,11,24));
makeVacationDay(date(2016,11,25));
makeVacationDay(date(2016,12,26));
makeVacationDay(date(2016,12,27));
makeVacationDay(date(2016,12,28));
makeVacationDay(date(2016,12,29));
makeVacationDay(date(2016,12,30));
makeVacationDay(date(2017,1,2));
makeVacationDay(date(2017,1,16));
makeVacationDay(date(2017,2,20));
makeVacationDay(date(2017,2,21));
makeVacationDay(date(2017,2,22));
makeVacationDay(date(2017,2,23));
makeVacationDay(date(2017,2,24));
makeVacationDay(date(2017,4,10));
makeVacationDay(date(2017,4,11));
makeVacationDay(date(2017,4,12));
makeVacationDay(date(2017,4,13));
makeVacationDay(date(2017,4,14));
makeVacationDay(date(2017,4,17));
makeVacationDay(date(2017,4,18));
makeVacationDay(date(2017,5,29));
makeVacationDay(date(2017,6,8));
makeVacationDay(date(2017,6,12));
makeVacationDay(date(2017,6,26));






dateList= makeDateList(startDate,endDate,timedelta(days=-1));

print(len(dateList))

for k, v in sorted(dateList.items()):
    print k,v


today = date.today();
print today



print howManySchoolDaysRemain(today)
