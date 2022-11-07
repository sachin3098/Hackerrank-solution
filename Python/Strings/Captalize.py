problem Link:

https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

def solve(s):
   s = s.split(" ")
   return(" ".join(i.capitalize() for i in s))
