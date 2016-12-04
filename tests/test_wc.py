import unittest
import sys
import shutil, tempfile
from os import path
sys.path.append('../src')
from wc import *

class TestWC(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            f.write("""a bb2\t ccc_3
	               dddd@@@    eeeee***""")
        with open(path.join(self.test_dir, 'test2.txt'), 'w') as f:
            f.write("""word's""")

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_words(self):
        self.assertEquals(5, with_file(path.join(self.test_dir, 'test.txt'), word_count))

    def test_word_with_quote_should_be_one_word(self):
        self.assertEquals(1, with_file(path.join(self.test_dir, 'test2.txt'), word_count))
    
    def test_count_word_should_be_33(self):
        self.assertEquals(48, with_file(path.join(self.test_dir, 'test.txt'), char_count))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
