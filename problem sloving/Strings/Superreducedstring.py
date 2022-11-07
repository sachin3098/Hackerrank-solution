Problem Link:

https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def superReducedString(s):
    # Write your code 
    given = list(s)    
    index = 0
    while index < len(given) - 1:
        if given[index] == given[index + 1]:
            del given[index:index+1+1]
            index = 0
        else:
            index += 1                 
    return ''.join(given) if given else 'Empty String'
