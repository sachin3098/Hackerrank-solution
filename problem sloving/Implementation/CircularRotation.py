Problem Link:

https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true

import math
import os
import random
import re
import sys


def circularArrayRotation(a, k, queries):
    for i in range(k):
        p=a.pop()
        a.insert(0,p)
    arr=[]
    for j in queries:
        arr.append(a[j])
    return arr        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()