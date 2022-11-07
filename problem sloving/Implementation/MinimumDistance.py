Problem Link:

https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def minimumDistances(a):
    #already in problem you can obersve that i and j given
    # so we use two loops.
    
    distance=sys.maxsize
    for i in range(n):
        for j in range(i+1,n):
            
            if a[i]==a[j]:
                distance=min(distance, j-i)
                
    if distance==sys.maxsize:
        return -1
    else:
        return distance           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()