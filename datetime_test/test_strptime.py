from nose.tools import eq_

from datetime import datetime as dt

def test_reading_year_month_day():
    expected = dt(2012,04,26)
    actual   = dt.strptime('2012-04-26','%Y-%m-%d')
    eq_(actual, expected)

def test_day_out_of_range():
    try:
        dt.strptime('2012-04-31','%Y-%m-%d')
    except ValueError as ex:
        eq_(ex.message,'day is out of range for month')

def test_not_enough_data():
    try:
        dt.strptime('2012-04','%Y-%m-%d')
    except ValueError as ex:
        eq_(ex.message,'time data \'2012-04\' does not match format \'%Y-%m-%d\'')

def test_too_much_data():
    try:
        dt.strptime('2012-04-26T12:00:00','%Y-%m-%d')
    except ValueError as ex:
        eq_(ex.message,'unconverted data remains: T12:00:00')
