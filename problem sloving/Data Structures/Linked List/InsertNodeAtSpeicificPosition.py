Problem Link:

https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?isFullScreen=true

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    current = llist
    new_node = SinglyLinkedListNode(data)
    for x in range(position-1):
        current = current.next
    new_node.next = current.next
    current.next = new_node
    
    return llist