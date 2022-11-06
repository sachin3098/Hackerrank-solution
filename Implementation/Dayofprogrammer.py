Problem Link:

https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

def dayOfProgrammer(year):
    # Write your code here
    if year<1918:
        if year%4==0:
            return (f"12.09.{year}")
        else:
            return (f"13.09.{year}")
    elif year>1918:
            if (year%400==0 or (year%4==0 and year%100!=0)):
                return (f"12.09.{year}")
            else:
                return (f"13.09.{year}")
    elif year==1918:
                return ("26.09.1918")