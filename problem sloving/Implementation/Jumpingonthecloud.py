Problem Link:

https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    jump=0
    i=0
    
    # we take i+2 first because we have to return minimum steps
    while i<n-1:
        if i+2<n and c[i+2]==0:
            jump+=1
            i+=2
            
        elif i+1<n and c[i+1]==0:
            jump+=1
            i+=1
       
    return jump        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
