Problem Link:

https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true

def divisibleSumPairs(n, k, ar):
    # Write your code here
    count=0
    for i in  range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if ((ar[i]+ar[j])%k)==0:
                count+=1
    return count     