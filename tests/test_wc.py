import unittest
import sys
sys.path.append('../src')
from wc import wc

class TestWC(unittest.TestCase):
    def test_words(self):
        text = """a bb2\t ccc_3
	dddd@@@    eeeee***"""
        self.assertEquals(5, wc(text))

    def test_word_with_quote_should_be_one_word(self):
        text = """word's"""
        self.assertEquals(1, wc(text))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
