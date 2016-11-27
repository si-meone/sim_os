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

def wc(text):
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
    
    arg1 = ''
    if len(sys.argv) > 1: 
        arg1 = sys.argv[1]
        logging.debug('opening file {}...'.format(arg1,))
    	print wc(open_file(arg1))
    else:
        print 'no file was specified' 
