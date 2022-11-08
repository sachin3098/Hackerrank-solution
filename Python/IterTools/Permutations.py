Problem Link:

https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations
s=input().split()
string=sorted(s[0])
number=int(s[1])

print(*list(map("".join,permutations(string,number))),sep="\n")