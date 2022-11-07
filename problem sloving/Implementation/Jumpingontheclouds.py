Problem Link:

https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true


import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    i = k % n
    energy = 100
    
    while (i != 0):
        if c[i] == 1:
            energy -= 2
        energy -= 1
        i = (i + k) % n
        
    return energy - 1 if c[0] == 0 else energy - 3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()