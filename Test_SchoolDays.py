import unittest
import howManyDays
import SchoolDaysUtils
from datetime import date
from datetime import datetime
import json

if __name__ == '__main__':
    unittest.main()


class TestSchoolDays(unittest.TestCase):
    def test_is_weekend(self):
        knownWeekDay = date(2017, 4, 6)
        knownWeekEnd = date(2017, 4, 8)
        self.assertTrue(SchoolDaysUtils.isWeekend(knownWeekEnd))
        self.assertFalse(SchoolDaysUtils.isWeekend(knownWeekDay))


    def test_get_enddate(self):
        with open('SchoolDataNYC20162017.json') as data:
            dates = json.load(data)
            enddate = howManyDays.getEndDay(dates)
            self.assertEqual(enddate,datetime(2017,06,28,0,0))


    def test_num_days_remaining(self):
         one_left = date(2017,06,27);
         fourty_eight_left = date(2017,04,06)
         self.assertEqual(howManyDays.numDaysRemaining(one_left),1)
         self.assertEqual(howManyDays.numDaysRemaining(fourty_eight_left), 48)

    def test_when_is_last_day(self):
        last_day = datetime(2017,6,28)
        self.assertEqual(howManyDays.whenIsLastDay(),last_day)

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