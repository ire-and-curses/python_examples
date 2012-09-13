#!/usr/bin/env python

from __future__ import division

from nose.tools import assert_equal, raises


from compress import compress, is_valid, InvalidInputError


class TestCompress(object):

    def setup(self):
        pass

    # Validation tests
    def test_rejects_empty_string(self):      assert_equal(is_valid(''),   False)
    def test_rejects_spaces(self):            assert_equal(is_valid('A '), False)
    def test_rejects_lowercase_letters(self): assert_equal(is_valid('Ab'), False)
    def test_rejects_numbers(self):           assert_equal(is_valid('A9'), False)
    def test_accepts_uppercase_letters(self): assert_equal(is_valid('AB'), True)

    @raises(InvalidInputError)
    def test_raises_exception_if_invalid_input(self): compress('abc1 D')


    def test_single_char(self):         assert_equal(compress('A'),       'A')
    def test_single_chars(self):        assert_equal(compress('ABAC'),    'ABAC')
    def test_zero_compress(self):       assert_equal(compress('AA'),      'AA0')
    def test_zero_none_compress(self):  assert_equal(compress('AAB'),     'AA0B')
    def test_zero_compress_twice(self): assert_equal(compress('AABB'),    'AA0BB0')
    def test_complex_compress(self):    assert_equal(compress('AAACBBC'), 'AA1CBB0C')


    # Example long runs
    def test_ten_repeat(self):      assert_equal(compress('AAAAAAAAAA'),     'AA8')
    def test_eleven_repeat(self):   assert_equal(compress('AAAAAAAAAAA'),    'AA9')
    def test_twelve_repeat(self):   assert_equal(compress('AAAAAAAAAAAA'),   'AA9A')
    def test_thirteen_repeat(self): assert_equal(compress('AAAAAAAAAAAAA'),  'AA9AA0')
    def test_fourteen_repeat(self): assert_equal(compress('AAAAAAAAAAAAAA'), 'AA9AA1')
