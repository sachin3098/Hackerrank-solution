Problem Link:

https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true

import math
import os
import random
import re
import sys

from collections import Counter
def matchingStrings(stringList, queries):
    # Write your code here
    s=Counter(stringList)
    result=[]
    
    for q in queries:
        result.append(s[q])
    return result    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()