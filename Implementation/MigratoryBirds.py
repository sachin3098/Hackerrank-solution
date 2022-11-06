Problem Link:

https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

def migratoryBirds(arr):
    # Write your code here
    table={}
    for ele in arr:
        if ele in table:
            table[ele]+=1
        else:
            table[ele]=1
    maxvalue=max(table.values())
    maxkeys=[k for k in table.keys() if table[k]==maxvalue]
    
    return min(maxkeys)