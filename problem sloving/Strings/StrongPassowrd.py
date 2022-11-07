Problem Link:

https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers="0123456789"
    lower_case="abcdefghijklmnopqrstuvwxyz"
    upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters="!@#$%^&*()-+"
    res = 0

    if not any(x in numbers for x in password):
        res += 1
    
    if not any(x in lower_case for x in password):
        res += 1

    if not any(x in upper_case for x in password):
        res += 1

    if not any(x in special_characters for x in password):
        res += 1

    if len(password) < 6:
        return max(res, 6 - len(password))
    
    return res  
                
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
