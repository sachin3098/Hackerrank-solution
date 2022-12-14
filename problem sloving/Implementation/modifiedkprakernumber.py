problem Link:

https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    result=[]
    
    for i in range(p,q+1):
        sqr=str(i**2)
        n=len(sqr)
        
        if i==1:
            result.append(i)
        
        elif n>1 and i==int(sqr[:n//2])+int(sqr[n//2:]):
            result.append(i)
            
    if len(result)==0:
        print("INVALID RANGE")
    else:
        print(*result)            

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
