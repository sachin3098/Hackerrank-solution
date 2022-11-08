Problem Link:

https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem?isFullScreen=true


def insertNodeAtTail(head, data):
    
    #create node
    node=SinglyLinkedListNode(data)
    
#case-1 if head pointer is null
    if head==None:
        head=node
    else:
#case-2 insert node at tail
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=node
    return head 