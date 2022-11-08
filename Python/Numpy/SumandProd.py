Problem Link:

https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true

import numpy
N,M=list(map(int, input().split()))
arr=numpy.array([input().split() for _ in range(N)],int)
z=numpy.sum(arr,axis=0)
print(numpy.prod(z))