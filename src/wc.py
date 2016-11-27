#!/usr/bin/env python
import re
import sys
import logging
from collections import Counter
import string
import argparse


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
   

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('file_name', metavar='F', type=str,
                    help='File name for counting')
    parser.add_argument('-l', dest='line_count',  action='store_true', help='lines in file')
    parser.add_argument('-m', dest='char_count',  action='store_true', help='words in file')

    args = parser.parse_args()
    print args
 
    if args.char_count: 
        logging.debug('opening file for char count {}...'.format(args.char_count))
        print char_count(open_file(args.file_name))
    elif args.line_count: 
        logging.debug('opening file for line count {}...'.format(args.line_count))
        print line_count(args.file_name)
    elif args.file_name: 
        logging.debug('opening file for word count {}...'.format(args.file_name))
    	print word_count(open_file(args.file_name))
    else:
        print 'No file specifed or params'
