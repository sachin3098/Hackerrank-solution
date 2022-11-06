Problem Link:

https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    x = 0
    height = 1
    while x <= n:
        if x == 0:
            height = 1
        elif x%2 !=0:
            height *= 2
        elif x%2 == 0:
            height += 1
        x += 1
    return height

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()