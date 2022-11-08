Problem Link:

https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem?isFullScreen=true

def printLinkedList(node):
    while node:
        print(node.data)
        node=node.next