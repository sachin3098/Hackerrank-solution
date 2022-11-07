problem Link:

https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    total_likes=0
    shared=5
    
    for i in range(n):
        like=shared//2
        total_likes+=like
        shared=3*like
        
    return total_likes    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()