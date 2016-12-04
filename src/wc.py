#!/usr/bin/env python
import re
import os
import sys
import logging
from collections import Counter
import string
import argparse


WORD = '\w+'
SYMBOLS = string.punctuation

def with_file(file_name, callback):
    with open(file_name, 'r') as f:
        return callback(f)

def line_count(f):
    logging.debug('file object: [{}]'.format(f.name))
    return len(f.readlines())

def char_count(f):
    logging.debug('file object: [{}]'.format(f.name))
    return len(f.read())

def byte_count(f):
    f.seek(0,2)
    byte_size = f.tell()
    return byte_size

def word_count(f):
    text = f.read()
    pat = re.compile(WORD) 
    logging.debug('original text: [{}]'.format(text))
    clean_text = text.translate(None, string.punctuation)
    logging.debug('translated text: [{}]'.format(clean_text))
    words = pat.findall(clean_text) 
    return len(words)    

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    level = logging.INFO
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=level)
    logging.debug('Started DEBUG')
    logging.debug('args {}'.format(sys.argv))
   

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('file_name', metavar='file', type=str,
                    help='File name for counting')
    parser.add_argument('-c', dest='byte_count',  action='store_true', help='bytes in file')
    parser.add_argument('-l', dest='line_count',  action='store_true', help='lines in file')
    parser.add_argument('-m', dest='char_count',  action='store_true', help='characters in file')
    parser.add_argument('-w', dest='word_count',  action='store_true', help='words in file')

    args = parser.parse_args()
    logging.debug('parser.parse_args() = {}'.format(args))
 
    if args.byte_count: 
        print with_file(args.file_name, byte_count)
        logging.debug('opening file for byte count {}...'.format(args.file_name))
    elif args.line_count: 
        logging.debug('opening file for line count {}...'.format(args.file_name))
        print with_file(args.file_name, line_count)
    elif args.char_count: 
        logging.debug('opening file for char count {}...'.format(args.file_name))
        print with_file(args.file_name, char_count)
    elif args.word_count: 
        logging.debug('opening file for word count {}...'.format(args.file_name))
        print with_file(args.file_name, word_count)
    elif args.file_name: 
        logging.debug('opening file for all line, words and character count {}...'.format(args.file_name))
        print '{} {} {}'.format(with_file(args.file_name, line_count), 
              with_file(args.file_name, word_count),
              with_file(args.file_name, char_count))
    else:
        print 'No file specifed or params'
