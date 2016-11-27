import unittest
import sys
sys.path.append('../src')
from wc import *

class TestWC(unittest.TestCase):
    def test_words(self):
        text = """a bb2\t ccc_3
	dddd@@@    eeeee***"""
        self.assertEquals(5, word_count(text))

    def test_word_with_quote_should_be_one_word(self):
        text = """word's"""
        self.assertEquals(1, word_count(text))
    
    def test_count_word_should_be_33(self):
        text = """a bb2\t ccc_3
	dddd@@@    eeeee***"""
        self.assertEquals(33, char_count(text))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
