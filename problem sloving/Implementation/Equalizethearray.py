Problem Link:

https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true

import math
import os
import random
import re
import sys

# we use counter to aviod creating dictionary manually.
from collections import Counter
def equalizeArray(arr):
    c=Counter(arr)
    return len(arr)-max(c.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()