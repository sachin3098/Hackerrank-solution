Problem Link:

https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

from itertools import combinations

N = int(input())
letters = input().split()
K = int(input())
combs = combinations(letters,K)
bool_list = [("a" in c) for c in combs]
sum_ , len_ = sum(bool_list),len(bool_list)
print(sum_/len_)
