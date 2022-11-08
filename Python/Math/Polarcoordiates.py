Problem Link:

https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

import cmath
c=complex(input().strip())
for i in cmath.polar(c):
    print(i)
