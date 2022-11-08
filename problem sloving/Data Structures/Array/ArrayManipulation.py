Problem Link:

https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    #initialize the array with zeros
    
    arr=[0]*(n+2)
    
    #perform the query operations
    for a,b,k in queries:
        arr[a]+=k
        arr[b+1]-=k
        
    #find max element from the array
    maximum=temp=0
    for val in arr:
        temp+=val
        maximum=max(maximum,temp)
        
    return maximum    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []