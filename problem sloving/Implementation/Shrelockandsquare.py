Problem Link:

https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true

import math
import os
import random
import re
import sys

from math import *
def squares(a, b):
    return floor(sqrt(b))-ceil(sqrt(a))+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()