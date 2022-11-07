Problem Link:

https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true

import math
import os
import random
import re
import sys

from collections import Counter

def cutTheSticks(arr):
    result=[]
    n=len(arr)
    s=Counter(arr)
    
    for i in sorted(s.keys()):
        result.append(n)     #we write this line here to continue loop
        n-=s[i]

    return result    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()