Problem Link:

https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    count=0
    for i,j in zip(s,t):
        if i==j:
            count+=1
        else:
            break
        
    t_len=len(s)+len(t)
    if t_len<=2*count+k and t_len%2==k%2 or t_len<k:
        return "Yes"
    else:
        return "No"        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()