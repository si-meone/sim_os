import unittest
import sys
sys.path.append('../src')
from wc import wc

class TestWC(unittest.TestCase):
    def test_wc(self):
        self.assertEquals("1", str(wc('t')))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
