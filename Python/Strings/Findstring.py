Problem Link:

https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
    counter=0
    l=len(sub_string)
    for i in range(0,len(string)):
        s=string[i:i+l]
        if s==sub_string:
            counter+=1
    return counter    