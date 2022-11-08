Problem Link:

https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import OrderedDict
n=int(input())
od=OrderedDict()
    
for i in  range(n):
    str=input().split()

    #our string is our key & all position before position (-1)
    k=" ".join(str[:-1]) 
    #value is at position.
    v=int(str[-1])       
    if k in od:
        od[k]=od[k]+v
    else:
        od[k]=v 