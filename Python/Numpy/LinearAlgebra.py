Problem Link:

https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true

import numpy
n=int(input())
a=numpy.array([input().split() for _ in range(n)],float)
print(round(numpy.linalg.det(a),2))
