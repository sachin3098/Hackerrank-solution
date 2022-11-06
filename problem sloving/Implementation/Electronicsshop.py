problem Link:

https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    options = [k+d for k in keyboards for d in drives if k+d <= b]
    return -1 if len(options) == 0 else max(options)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))