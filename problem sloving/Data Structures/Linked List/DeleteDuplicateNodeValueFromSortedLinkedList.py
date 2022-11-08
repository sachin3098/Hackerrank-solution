Problem Link:

https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem?isFullScreen=true

def removeDuplicates(llist):
    node = llist
    while node.next:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return llist