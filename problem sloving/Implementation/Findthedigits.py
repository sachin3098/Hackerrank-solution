Problem Link:

https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def findDigits(n):
    number= str(n)
    count=0
    
    for ch in number:
        try:
            if n % int(ch) == 0:
                count += 1
        except:
            ZeroDivisionError()
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()