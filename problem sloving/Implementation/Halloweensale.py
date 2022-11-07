problem Link:

https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def howManyGames(p, d, m, s):
    total=0
    
    while p<=s:
        s-=p
        p=max(p-d,m)
        total+=1
    return total    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()