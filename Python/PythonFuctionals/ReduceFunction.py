Problem Link:

https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true

def product(fracs):
    t = reduce(lambda x,y:x*y,fracs)
    return t.numerator, t.denominator