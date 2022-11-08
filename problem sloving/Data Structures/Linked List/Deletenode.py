Problem Link:

https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem?isFullScreen=true

def deleteNode(head, position):
    # Write your code here
    
    if position==0:
        head=head.next
    else:
        temp=head
        count=1
        while temp!=None and count<position:
            temp=temp.next
            count+=1
         
        #delete node
        temp.next=temp.next.next