Problem Link:

https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def camelcase(s):
    # Write your code here
    camm=0
    for ch in s:
        if ch.isupper() == True:
            camm+=1
            
    return camm+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()