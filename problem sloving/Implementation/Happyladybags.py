problem Link:

https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true


import math
import os
import random
import re
import sys

def happyLadybugs(b):
    if '_' in b:
        for color in set(b) - {'_'}:
            if b.count(color) == 1:
                return 'NO'
    else:
        if len(b) == 1 or b[0] != b[1] or b[-1] != b[-2]:
            return 'NO'
        for i in range(1, len(b)-1):
            if b[i-1] != b[i] and b[i] != b[i+1]:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()