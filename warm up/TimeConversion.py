Problem Link:

https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

def timeConversion(s):
    if s[-2:]=="AM" and s[:2]=="12":
          return "00"+s[2:-2]
    elif s[-2:]=="PM" and s[:2]!="12":
          ans=int(s[:2])+12
          return str(str(ans)+s[2:-2])
    else:
     return s[:-2]
