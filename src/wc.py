#!/usr/bin/env python
import re
import sys
import logging
from collections import Counter
import string

WORD = '\w+'
SYMBOLS = string.punctuation

def open_file(file_name):
    with open(file_name, 'r') as f:
       return f.read()

def line_count(file_name):
    with open(file_name, 'r') as f:
        return len(f.readlines())

def char_count(text):
    logging.debug('original text: [{}]'.format(text))
    return len(text)

def word_count(text):
    pat = re.compile(WORD) 
    logging.debug('original text: [{}]'.format(text))
    clean_text = text.translate(None, string.punctuation)
    logging.debug('translated text: [{}]'.format(clean_text))
    words = pat.findall(clean_text) 
    return len(words)    

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    level = logging.DEBUG
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=level)
    logging.debug('Started DEBUG')
    logging.debug('args {}'.format(sys.argv))
    
    arg1 = ''
    if len(sys.argv) == 2: 
        arg1 = sys.argv[1]
        logging.debug('opening file for word count {}...'.format(arg1,))
    	print word_count(open_file(arg1))
    elif len(sys.argv) == 3 and sys.argv[1] == '-m': 
        arg2 = sys.argv[2]
        logging.debug('opening file for char count {}...'.format(arg2,))
        print char_count(open_file(arg2))
    elif len(sys.argv) == 3 and sys.argv[1] == '-l': 
        arg2 = sys.argv[2]
        logging.debug('opening file for char count {}...'.format(arg2,))
        print line_count(arg2)
    else:
        print 'no file was specified or args' 
