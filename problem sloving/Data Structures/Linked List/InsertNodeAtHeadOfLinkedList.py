Problem Link:

https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem?isFullScreen=true

def insertNodeAtHead(head, data):
    # Write your code here
    node=SinglyLinkedListNode(data)
    
    if head!=None:
        node.next=head
        
    return node