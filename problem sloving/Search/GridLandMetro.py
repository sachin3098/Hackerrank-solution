Problem Link:

https://www.hackerrank.com/challenges/gridland-metro/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def gridlandMetro(n, m, k, track):
    # Write your code here
    d={}
    total=n*m
    
    for i in range(k):
        r=track[i][0]
        c1=track[i][1]
        c2=track[i][2]
        
    #if track not present
        if r not in d:
           d[r]=[c1,c2]
    # if track not overlapping then update total
        elif c1>d[r][1]:
           total -= c2-c1+1
    # if track is overlapping then update total
        elif c2>d[r][1]:
            d[r][1]=c2
        
    tracks=0
    for r in d:
        tracks+=d[r][1]-d[r][0]+1
        
    lamps=total-tracks
    return lamps    
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()