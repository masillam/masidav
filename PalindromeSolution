import sys
import random
import sys
data=sys.stdin.readlines()
arr1 = [x.replace('\n', '') for x in data]

#arr=["archit","ar","aaaaa","bbb"]

firstchar = arr1[0]
n = int(firstchar)

arr=[x.replace(' ', '') for x in arr1][1:]

MAX_CHAR = 26

import sys

def findAndPrintUncommonChars(str1, str2):

  diffset=set(str1)-set(str2)
  uncomstr=random.choice(tuple(diffset))

  return uncomstr

it = iter(arr)
for x in it:
  S1,S2= x, next(it)

  uncommon=findAndPrintUncommonChars(S1, S2)[0]
  S3 = S2 + uncommon
  set1 = set(S1)-set(S2)

  if len(set1)>1:

    txt = S3[::-1]
    S4 = S3 + txt
    difference=set(S1)-set(S4)
    print len(difference)


  else:
    S5=uncommon+S2+uncommon
    print sum ( S5[i] != S1[i] for i in range(len(S5)) )
