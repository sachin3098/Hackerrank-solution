#Link 

https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    # Write your code here
    x=sum(arr)
    minsum=x-max(arr)
    maxsum=x-min(arr)
    print(minsum,maxsum)
