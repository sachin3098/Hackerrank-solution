Problem Link:

https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem?isFullScreen=true

def has_cycle(head):
    #initialize two points
    slow=fast=head
    
    #main logic
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        
        #check if both pointers are same
        if slow==fast:
            return True
        
    return False 