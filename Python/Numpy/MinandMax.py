Problem Link:

https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true

import numpy
N,M=list(map(int, input().split()))
arr=numpy.array([input().split() for _ in range(N)],int)
z=numpy.min(arr,axis=1)
print(numpy.max(z))