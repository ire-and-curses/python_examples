#!usr/bin/env/python

from nose.tools import assert_equal

from compression.compressor import compress

class TestCompressor(object):
    
    def test_one(self):
        input = 'A'
        output = compress(input)
        expected = 'A'
        assert_equal(output, expected)
    
    def test_two(self):
        input = 'AA'
        output = compress(input)
        expected = 'AA0'
        assert_equal(output, expected)
        
    def test_three(self):
        input = 'AAA'
        output = compress(input)
        expected = 'AA1'
        assert_equal(output, expected)
        
    def test_four(self):
        input = 'AAAA'
        output = compress(input)
        expected = 'AA2'
        assert_equal(output, expected)    
          
    def test_ten(self):
        input = 'AAAAAAAAAA'
        output = compress(input)
        expected = 'AA8'
        assert_equal(output, expected)
        
    def test_eleven(self):
        input = 'AAAAAAAAAAA'
        output = compress(input)
        expected = 'AA9'
        assert_equal(output, expected)
        
    def test_twelve(self):
        input = 'AAAAAAAAAAAA'
        output = compress(input)
        expected = 'AA9A'
        assert_equal(output, expected)
        
    def test_thirteen(self):
        input = 'AAAAAAAAAAAAA'
        output = compress(input)
        expected = 'AA9AA0'
        assert_equal(output, expected)    
                    
    def test_fourteen(self):
        input = 'AAAAAAAAAAAAAA'
        output = compress(input)
        expected = 'AA9AA1'
        assert_equal(output, expected)

        
    def test_single_mixed(self):
        input = 'ABAC'
        output = compress(input)
        expected = 'ABAC'
        assert_equal(output, expected)  
        
    def test_double_mixed(self):
        input = 'AAB'
        output = compress(input)
        expected = 'AA0B'
        assert_equal(output, expected)  
        
    def test_mixed_repeat(self):
        input = 'AABB'
        output = compress(input)
        expected = 'AA0BB0'
        assert_equal(output, expected)
        
    def test_mixed(self):
        input = 'AAACBBC'
        output = compress(input)
        expected = 'AA1CBB0C'
        assert_equal(output, expected)
        
    def test_over_nine_mixed(self):
        input = 'AAAAAAAAAAAAABBBBBCCCCCCCCCCCDFGGGCC'
        output = compress(input)
        expected = 'AA9AA0BB3CC9DFGG1CC0'
        assert_equal(output, expected)
        
    
