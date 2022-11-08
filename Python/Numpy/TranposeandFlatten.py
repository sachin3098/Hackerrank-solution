Problem Link:

https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true

import numpy

N,M=list(map(int,input().split()))

a = numpy.array([input().split() for _ in range(N)], int)

print(a.transpose())
print(a.flatten())
