problem link:

https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def acmTeam(topic):
    maxsub=0
    count=0
    
    #use of for loop in no.of attendee 
    for i in range(n):
        #use of for loop in binary string
        for j in range(i,n):
            
            sub=0
            #for both for loop run run simultaneously
            for x,y in zip(topic[i],topic[j]):
            
                if x=="1" or y=="1":
                    sub+=1
             
            if sub>maxsub:
                maxsub=sub
                count=1
                
            elif sub==maxsub:
                count+=1
                
    return [maxsub,count]            
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()