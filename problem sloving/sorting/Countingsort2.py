Problem Link:

https://www.hackerrank.com/challenges/countingsort2/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def countingSort(arr):
    # Write your code here
    freq_arr = [0]*100 
    for a in arr:
        freq_arr[a]+=1

    sorted_arr = []    
    for i in range(100):
        sorted_arr.extend( [i]*freq_arr[i] )
    return sorted_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
