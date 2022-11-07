Problem Link:

https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def hackerrankInString(s):
    # Write your code here

    if re.match(r'.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*', s):
        return 'YES'
    else:
        return 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()