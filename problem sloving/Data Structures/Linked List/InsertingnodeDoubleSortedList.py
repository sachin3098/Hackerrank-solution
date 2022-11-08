Problem Link:

https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?isFullScreen=true

def sortedInsert(head, data):
    # create the node
    node=DoublyLinkedListNode(data)
    
    #cas-1 list is empty
    if head==None:
        head=node
    
    #case-2 insert before head
    elif data<head.data:
        node.next=head
        head.prev=node
        head=node