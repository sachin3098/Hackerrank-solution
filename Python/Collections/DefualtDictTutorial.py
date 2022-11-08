Problem Tutorial:

https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict

# Inputs
# ------
n, m = map(int, input().split(' '))

# Let's get the groups as lists
# -----------------------------
#input1 = ['a', 'a', 'b', 'a', 'b']
#input2 = ['a', 'b']
input1 = list()
for i in range(n):
    input1.append(input())