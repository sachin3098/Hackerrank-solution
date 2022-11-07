Problem Link:

https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true

import math
import os
import random
import re
import sys


from collections import Counter
def missingNumbers(arr, brr):
    # Write your code here
    c1=Counter(arr)
    c2=Counter(brr)
    c=c2-c1
    
    return sorted(c.keys())
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()