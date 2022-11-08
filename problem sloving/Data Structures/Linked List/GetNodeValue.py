Problem Link:

https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem?isFullScreen=true

def getNode(head, positionFromTail):
    # Write your code here
    ptr1=head
    ptr2=head
    
    #tranverse to the position from the head
    for i in range(positionFromTail):
        ptr1=ptr1.next
        
    #tranverse both pointers
    while ptr1.next!=None:
        ptr1=ptr1.next
        ptr2=ptr2.next
        
    return ptr2.data 