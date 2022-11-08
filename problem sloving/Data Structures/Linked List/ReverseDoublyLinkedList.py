Problem Link:

https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?isFullScreen=true

def reverse(head):
    while head.next!=None:
        
        #swap the pointer
        head.next,head.prev,head=head.prev,head.next,head.next
        
    #change to the tail node    
    head.next,head.prev=head.prev,None
    return head
        