Problem Link:

https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import Counter
def sherlockAndAnagrams(s):
    count=0
    dic=Counter(s)
    for i in range(2,len(s)):
        sb=s[0:i]
        l=len(sb)
        dic["".join(sorted(sb))]+=1
        for j in range(1,len(s)):
            if j+l<=len(s):
                dic["".join(sorted(s[j:j+l]))]+=1
                
    print(dic)
    for k,v in dic.items():
        count+=v*(v-1)//2
    return count            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()