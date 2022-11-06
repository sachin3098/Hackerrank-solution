problem Link:

https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

def breakingRecords(scores):
    # Write your code here
    high = scores[0]
    low = scores[0]
    h, l = 0, 0
    for i in scores:
        if i > high:
            high = i
            h+=1
        elif i < low:
            low = i
            l+=1
    return h,l