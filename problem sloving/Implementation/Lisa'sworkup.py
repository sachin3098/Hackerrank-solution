Problem Link:

https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def workbook(n, k, arr):
    answer=0
    page=1
    
    for probs in arr:
        for index in range(1,probs+1):
            if index==page:
                answer+=1
                
            if index==probs or index%k==0:
                page+=1
                
    return answer        
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
