problem Link:

https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))
    