Problem Link:

https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem?isFullScreen=true


import sys
sys.setrecursionlimit(100000)

def mergeLists(head1, head2):
    #check both linked list head none or not
    if head1==None and head2==None:
        return None
    
    if head1==None:
        return head2
    if head2==None:
        return head1