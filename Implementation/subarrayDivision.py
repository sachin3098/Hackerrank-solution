Problem Link:

https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true

def birthday(s, d, m):
    i=0
    j=m
    count=0
    while j<=len(s):
        if sum(s[i:j])==d:
             count+=1
        i+=1
        j+=1
    return count 