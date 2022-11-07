Problem Link:

https://www.hackerrank.com/challenges/the-love-letter-mystery/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def theLoveLetterMystery(s):
    # Write your code here
    c=0
    for i in range(len(s)//2):
        if s[i]!=s[-(i+1)]:
            c+=abs(ord(s[i])-ord(s[-(i+1)]))
    return c 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()