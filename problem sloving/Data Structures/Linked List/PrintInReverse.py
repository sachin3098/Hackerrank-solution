Problem Link:

https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem?isFullScreen=true

def reversePrint(head):
    # Write your code here
    
    if head==None:
        return
    
    reversePrint(head.next)
    print(head.data)