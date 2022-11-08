Problem Link:

https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true

import numpy
N,M=list(map(int, input().split()))
a=numpy.array([input().split() for _ in range(N)],int)
b=numpy.array([input().split() for _ in range(N)],int)
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')