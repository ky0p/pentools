#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################################
#                Autox0r 0.1 / ky0p - 2014                #
###########################################################
# xor with a key and string/file                          #
###########################################################

import sys
import argparse

#Convert a string into a Byte Array
def str2ByteArray(str):
    strByteArray = []
    for i in str:
        strByteArray.append(ord(i))
    return strByteArray

#Xor file data with key
def xor(data, key):
    l = len(key)
    return bytearray(((data[i] ^ key[i % l]) for i in range(0,len(data))))

#We parse args in here
parser = argparse.ArgumentParser(description='xor a key with something.')
parser.add_argument('-k','--key', help='key to xor something with', dest='key', required=True)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f','--file', dest='file', help='if you want to xor a file, choose this option')
group.add_argument('-s','--string', dest='string', help='if you want to xor with a string, choose this option')

args = parser.parse_args()

key = bytearray(str2ByteArray(args.key))
encoded_key = str(bytearray(str(str2ByteArray(args.key))))
print u"key : "+args.key
print u"key (encoded) : "+encoded_key

if args.file:
  data = bytearray(open(args.file, 'rb').read())
  print u"xor with file \""+ args.file + "\""
  result = xor(data,key)

if args.string:
  data = bytearray(str2ByteArray(args.string))
  encoded_data = str(bytearray(str(str2ByteArray(args.string))))
  print u"xor with string : "+ args.string
  print u"xor with string (encoded) : " + encoded_data
  
result = xor(data,key)
encoded_result = str2ByteArray(str(result))
print result
print encoded_result

sys.exit(0)
