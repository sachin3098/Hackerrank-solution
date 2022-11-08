Problem Link:

https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

T = int(input())
for i in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))

    x = 0
    for i in range(n//2):
        if (blocks[i+1] > blocks[i] and blocks[i+1] > blocks[n-1-i]) or (blocks[n-1-i-1] > blocks[i] and blocks[n-1-i-1] > blocks[n-1-i]):
            x = 1
    
    if x == 1:
        print("No")
    else:
        print("Yes")