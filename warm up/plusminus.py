Problem Link:

https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

def plusMinus(arr):
    # Write your code here
    a,b,c=0,0,0
    for i in range(len(arr)):
        if arr[i]>0:
            a=a+1
        elif arr[i]<0:
            b=b+1   
        else:
            c=c+1
    print (a/len(arr))
    print (b/len(arr))
    print (c/len(arr))