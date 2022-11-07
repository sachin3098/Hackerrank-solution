problem Link:

https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

def wrap(string, max_width):
    s = ""
    for c in range(0,len(string),max_width):
        s += string[c:c+max_width] + "\n"
    return s
    