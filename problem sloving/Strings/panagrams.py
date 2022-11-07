Problem Link:

https://www.hackerrank.com/challenges/pangrams/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def pangrams(s):
    # Write your code here
    s=set(s.lower())
    if len(s)==27:
        return 'pangram'
    else:
        return 'not pangram'
    
           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()