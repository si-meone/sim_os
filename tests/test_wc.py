import unittest
import sys
sys.path.append('../src')
from wc import wc

class TestWC(unittest.TestCase):
    def test_wc(self):
        text = """a bb2\t ccc_3
	dddd@@@    eeeee***"""
        self.assertEquals(5, wc(text))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
