Problem Link:

https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math
AB=int(input())
BC=int(input())

print(round(math.degrees(math.atan(AB/BC))),chr(176),sep="")