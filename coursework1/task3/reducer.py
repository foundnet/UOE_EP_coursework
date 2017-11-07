#!/usr/bin/python

import sys

maxlength = 0
maxtokens = 0

for line in sys.stdin:
     slength,stokens = line.split("\t",1)
     length = int(slength)
     tokens = int(stokens)
     if length > maxlength:
         maxlength = length
     if tokens > maxtokens:
         maxtokens = tokens

print ("{0}\t{1}".format(maxlength,maxtokens))

