Problem Link:

https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true

l=[]
s=sorted(input())
lower=""
upper=""
digit=""
odd=""
even=""

for i in s:
    if i.islower():
        lower+=i
    elif i.isupper():
        upper+=i  
    elif int(i)%2!=0:
        odd+=i
    elif int(i)%2==0:
        even+=i
        
print(lower+upper+digit+odd+even)