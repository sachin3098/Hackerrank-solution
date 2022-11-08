Problem Link:

https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true

import numpy

N,M=list(map(int,input().split()))
a=numpy.array([input().split() for _ in range(N)],int)
print (numpy.mean(a,axis=1))
print (numpy.var(a,axis=0))
print (round(numpy.std(a,axis=None),11))
