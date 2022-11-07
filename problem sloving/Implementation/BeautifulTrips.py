Problem Link:

https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true

import math
import os
import random
import re
import sys

from collections import Counter
def beautifulTriplets(d, arr):
    
    m=Counter(arr)
    count=0
    
    for num in arr:
        if m[num+d] and  m[num+d+d]:
            count+=1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()