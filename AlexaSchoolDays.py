"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""
from datetime import datetime, timedelta, date
from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the NYC School Day Counter. " \
                    "Please ask me a question like how many days are left in the school year, " \
                    "or when is the last day of school?"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please ask me a question like how many days are left in the school year, " \
                    "or when is the last day of school?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the NYC School Day Counter. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}

def howManyDaysLeft(intent, session):
    """ Determines how many school days left.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    numDays = howManyLeft()
    speech_output = "There are " +numDays + " left in the school year"
    reprompt_text = "Try Again?"


    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))




def whatIsLastDay(intent, session):
    session_attributes = {}
    reprompt_text = None
    lastDay = whenIsLastDay();
    speech_output = "The last day of school in NYC is " + lastDay + \
                        ". Goodbye."
    should_end_session = True

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def i_hear_those_things(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = "It glides as softly as a cloud."
    should_end_session = True
    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "HowManyDaysLeft":
        return howManyDaysLeft(intent, session)
    elif intent_name == "WhatIsLastDay":
        return whatIsLastDay(intent, session)
    elif intent_name == "IHearThoseThingsAreAwfullyLoud":
        return i_hear_those_things(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


#School calendar specific code
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
