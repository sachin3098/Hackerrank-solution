Problem Link:

https://www.hackerrank.com/challenges/tutorial-intro/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def introTutorial(V, arr):
    # Write your code here
     return arr.index(V)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()