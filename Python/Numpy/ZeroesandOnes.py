Problem Link:

https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true

import numpy
nums = list(map(int, input().split()))
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))