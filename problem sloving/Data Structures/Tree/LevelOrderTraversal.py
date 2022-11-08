Problem Link:

https://www.hackerrank.com/challenges/tree-level-order-traversal/problem?isFullScreen=true

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

from collections import deque

def levelOrder(root):
    q=deque([root])
    
    #main logic
    while len(q):
        root=q.popleft()
        print(root,end=" ")
        
        #explore the next level
        if root.left:q.append(root.left)
        if root.right:q.append(root.right)