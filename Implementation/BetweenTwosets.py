problem Link:

https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true

def getTotalX(a, b):
    # Write your code here
    a_factors=[]
    b_factors=[]
    commom_numbers=[]
    max_len=len(a+b)
    
    for i in range(1,101):
        for number in a:
            if i%number==0:
                a_factors.append(i)
                
    for i in range(1,101):
        for number in b:
            if number%i==0:
                b_factors.append(i)
                
    temp=a_factors+b_factors
    
    for number in temp:
        if temp.count(number)==max_len:
            commom_numbers.append(number)
    
    return len(set(commom_numbers))       
            