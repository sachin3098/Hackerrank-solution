Problem Link:

https://www.hackerrank.com/challenges/mars-exploration/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def marsExploration(s):
    # Write your code here
    x=len(s)/3
    y=int(x)
    count=0
    z="SOS"*y
    for i in range(len(s)):
        if (s[i]!=z[i]):
            count+=1
    return count        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
