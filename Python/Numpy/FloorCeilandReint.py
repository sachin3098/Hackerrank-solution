Problem Link:

https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true

import numpy
numpy.set_printoptions(legacy="1.13")
arr=list(map(float,input().split()))
print(numpy.floor(arr),numpy.ceil(arr),numpy.rint(arr),sep="\n")