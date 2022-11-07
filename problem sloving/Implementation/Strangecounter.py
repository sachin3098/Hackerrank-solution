Problem Link:

https://www.hackerrank.com/challenges/strange-code/problem?isFullScreen=true


import math
import os
import random
import re
import sys

def strangeCounter(t):
    time=3
    while True:
        t-=time
        if t<=0:
            t+=time
            return time-t+1
        time*=2
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()