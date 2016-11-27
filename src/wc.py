#!/usr/bin/env python
import re
import sys
import logging


WORD = '\w+'

def open_file(file_name):
    with open(file_name, 'r') as f:
       return f.read()

def wc(text):
    pat = re.compile(WORD) 
    return len(pat.findall(text)) 

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    level = logging.INFO
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=level)
    logging.debug('Started DEBUG')
    
    arg1 = ''
    if len(sys.argv) > 1: 
        arg1 = sys.argv[1]
        logging.debug('opening file {}...'.format(arg1,))
    	print wc(open_file(arg1))
    else:
        print 'no file was specified' 
