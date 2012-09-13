from nose.tools import eq_
from datetime import datetime as dt

from dateutil import parser

def test_reading_iso_datetime():
    actual   = parser.parse('2012-04-26T12:00:00')
    expected = dt(2012,04,26,12,0)
    eq_( expected, actual )

def test_reading_bad_format():
    actual = parser.parse('2012-04-26 12:00')
    expected = dt(2012,04,26,12,0)
    eq_( expected, actual )
