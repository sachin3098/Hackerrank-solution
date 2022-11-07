Problem Link:

https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

n=int(input())        #no.of students.
res=[]
grade=[]

for i in range(n):
    name=input()
    mark=float(input())
    res.append([name,mark])
    grade.append(mark)
    

grade=sorted(set(grade))

m=grade[1]

name=[]
for val in res:          # for second lowest marks which name comes that we print.
    if m==val[1]:
        name.append(val[0])   
name.sort()