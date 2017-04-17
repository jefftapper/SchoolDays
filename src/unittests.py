import json
import unittest
from datetime import date
from datetime import datetime

import AlexaSchoolDays
import SchoolDaysUtils

import howManyDays

if __name__ == '__main__':
    unittest.main()


def mock_intent(arg, argType):
    intent = {'slots': {}}
    if not (arg is None):
        intent['slots'][argType] = {}
        intent['slots'][argType]['value'] = arg
    return intent


def get_output_speech(module, method, arg, argType):
    intent = mock_intent(arg, argType)
    session = {}
    answer = getattr(module, method)(intent, session)

    return answer['response']['outputSpeech']['text']


class TestSchoolDays(unittest.TestCase):
    def test_is_weekend(self):
        knownWeekDay = date(2017, 4, 6)
        knownWeekEnd = date(2017, 4, 8)
        self.assertTrue(SchoolDaysUtils.isWeekend(knownWeekEnd))
        self.assertFalse(SchoolDaysUtils.isWeekend(knownWeekDay))

    def test_get_enddate(self):
        with open('./resources/data/SchoolDataNYC20162017.json') as data:
            dates = json.load(data)
            enddate = howManyDays.getEndDay(dates)
            self.assertEqual(enddate, datetime(2017, 06, 28, 0, 0))

    def test_num_days_remaining(self):
        # noinspection PyTrailingSemicolon
        one_left = date(2017, 06, 27);
        fourty_eight_left = date(2017, 04, 06)
        self.assertEqual(howManyDays.numDaysRemaining(one_left), 1)
        self.assertEqual(howManyDays.numDaysRemaining(fourty_eight_left), 48)

    def test_when_is_last_day(self):
        last_day = datetime(2017, 6, 28)
        self.assertEqual(howManyDays.whenIsLastDay(), last_day)

    def test_is_there_school_on_date(self):
        known_school_days = [
            datetime(2017, 6, 27),
            datetime(2016, 9, 8),
            datetime(2017, 2, 27),
            datetime(2017, 6, 27),
            datetime(2016, 12, 23),
            datetime(2017, 1, 3),
            datetime(2017, 2, 17),
            datetime(2017, 4, 7),
            datetime(2017, 4, 19),
            datetime(2017, 6, 27)
        ]
        known_days_off = [
            datetime(2016, 9, 7),
            datetime(2016, 9, 10),
            datetime(2016, 9, 11),
            datetime(2016, 9, 12),
            datetime(2016, 12, 25),
            datetime(2016, 12, 26),
            datetime(2017, 1, 1),
            datetime(2017, 1, 2),
            datetime(2017, 2, 20),
            datetime(2017, 4, 10),
            datetime(2017, 4, 18),
            datetime(2017, 6, 29)
        ]

        for date in known_school_days:
            self.assertTrue(howManyDays.isThereSchoolOnDay(date.date()))

        for date in known_days_off:
            self.assertFalse(howManyDays.isThereSchoolOnDay(date.date()))

    def test_alexa_is_there_school(self):
        theDate = date.today()
        isThereSchool = howManyDays.isThereSchoolOnDay(theDate)

        firstResponse = get_output_speech(AlexaSchoolDays, "is_there_school", theDate, 'Date')
        if (isThereSchool):
            expectedResponse = "There is School on " + theDate.strftime('%B %d')
        else:
            expectedResponse = "There is not school on " + theDate.strftime('%B %d')
        self.assertEqual(firstResponse.lower(), expectedResponse.lower())

        # offDay = date(2016, 9, 7)
        # secondResponse = get_output_speech(AlexaSchoolDays, "is_there_school", offDay, 'Date')
        # second_expectedResponse = "There is not school on " + offDay.strftime('%B %d')
        # self.assertEqual(secondResponse.lower(), second_expectedResponse.lower())

    def test_alexa_whatIsLastDay(self):
        expected_last_day = date(2017, 6, 28)
        computed_last_day = get_output_speech(AlexaSchoolDays, "whatIsLastDay", None, None)
        expected_last_day_string = "The last day of school in NYC is " + expected_last_day.strftime("%B %d")
        self.assertEqual(computed_last_day, expected_last_day_string)

    def test_alexa_i_hear_those_things(self):

        computed_output = get_output_speech(AlexaSchoolDays, "i_hear_those_things", None, None)
        expected_output = "It glides as softly as a cloud."
        self.assertEqual(computed_output, expected_output)

    def test_alexa_how_many_left(self):
        expected_left = "There are " + str(howManyDays.howManyLeft()) + "days left in the school year"
        computed_left = get_output_speech(AlexaSchoolDays, "howManyDaysLeft", None, None)
        self.assertEqual(computed_left, expected_left)
