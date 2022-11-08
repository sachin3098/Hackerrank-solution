Problem Link:

https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true

import numpy
n = list(map(float,input().split()));
m = input();
print(numpy.polyval(n,int(m)));