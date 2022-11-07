Problem Link:

https://www.hackerrank.com/challenges/countingsort1/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def countingSort(arr):
    # Write your code here
    res=[0]*100
    for i in range(len(arr)):
        res[arr[i]]+=1
    return res

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()