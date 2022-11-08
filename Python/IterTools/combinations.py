problem Link:

https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true


from itertools import combinations
s=input().split()

#s[0] means first position.
string=sorted(s[0])
number=int(s[1])
for i in range(1,number+1):
    print(*list(map("".join,combinations(string,i))),sep="\n")