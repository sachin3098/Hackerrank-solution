Problem Link:

https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

from collections import Counter
n=int(input())
l=list()

for _ in range(n):
    l.append(input())
    
x=Counter(l)
print(len(x))
print(*x.values())