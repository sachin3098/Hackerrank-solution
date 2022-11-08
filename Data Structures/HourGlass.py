Problem Link:

https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    maxsum=-99
    
    for i in range(4):
        for j in range(4):
            #top value
            top=sum(arr[i][j:j+3])
            #middle value
            middle=arr[i+1][j+1]
            #bottom value
            bottom=sum(arr[i+2][j:j+3])
            
            totalsum=top+middle+bottom
            maxsum=max(totalsum,maxsum)
            
    return maxsum        
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()