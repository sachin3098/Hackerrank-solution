Problem Link:

https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    total=0
    
    for i in s:
        if i=="a":
            total+=1
            
     # when n is some integer.       
    total=n//len(s)*total
    
    #for remaining string
    for i in s[:n%len(s)]:
        if i=="a":
            total+=1
            
    return total        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()