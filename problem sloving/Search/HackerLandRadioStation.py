Problem Link:

https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def hackerlandRadioTransmitters(x, k):
    x.sort()
    count=0
    i=0
    
    #first half
    while i<n:
        loc=x[i]+k
        while i<n and x[i]<=loc:
            i+=1
    
    #place trasnmitter and incerment        
        i-=1
        count+=1
    #second half     
        loc=x[i]+k
        while i<n and x[i]<=loc:
            i+=1
        
    return count        
        
    print(count_trans)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()