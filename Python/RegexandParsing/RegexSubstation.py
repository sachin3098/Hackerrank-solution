Problem Link:

https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true

for _ in range(int(input())):
    line = input()
    
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    
    print(line)