Problem Link:

https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true

from itertools import combinations_with_replacement

s=input().split()
string=sorted(s[0])
number=int(s[1])
print(*list(map("".join,combinations_with_replacement(string,number))),sep="\n")