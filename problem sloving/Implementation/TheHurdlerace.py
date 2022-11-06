problem Link:

https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true

def hurdleRace(k, height):
    dose = max(height) - k
    
    # if does<=0 means no dose if does>0 take it.
    return 0 if dose <= 0 else dose
