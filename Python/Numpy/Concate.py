Problem Link:

https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true

import numpy

N,M,P=list(map(int, input().split()))
a=numpy.array([input().split() for _ in range(N+M)],int)
print(a)
