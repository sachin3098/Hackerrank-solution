Problem Link:

https://www.hackerrank.com/challenges/service-lane/problem?isFullScreen=true

import math
import os
import random
import re
import sys


def serviceLane(n, cases):
    result=[]
    
    # i= starting index and j=last indes
    for i,j in cases:
        result.append(min(width[i:j+1]))
        
    return result    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()