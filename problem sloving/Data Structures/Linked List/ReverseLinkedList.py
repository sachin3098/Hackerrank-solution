Problem Link:

https://www.hackerrank.com/challenges/reverse-a-linked-list/problem?isFullScreen=true

def reverse(head):
    # Write your code here
    prev=None
    cur=head
    next=head.next
    
    while cur!=None:
        next=cur.next
        
        #change the direction of node
        
        cur.next=prev
        #shifting the nodes
        prev=cur
        cur=next
        
    head=prev
    return head