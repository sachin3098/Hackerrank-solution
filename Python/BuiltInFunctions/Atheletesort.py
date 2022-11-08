Problem Link:

https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true

import math
import os
import random
import re
import sys


if __name__ == '__main__':
   n_m = list(map(int, input().split()))

table = list()

for i in range(n_m[0]):
    table.append(list(map(int, input().split())))
    
k = int(input())

sorted_table = sorted(table, key=lambda record: record[k])

for item in sorted_table:
    print(*item)