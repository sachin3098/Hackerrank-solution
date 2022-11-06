Problem Link:

https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

def diagonalDifference(arr):

    sum1=0
    sum2=0
    for i in range(len(arr)):
        sum1=sum1+arr[i][i]
        sum2=sum2+arr[i][-i-1]
    return (abs(sum1-sum2))   