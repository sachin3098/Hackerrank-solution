Problem Link:

https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?isFullScreen=true

def height(root):
    if root==None:
        return -1
    else:
        return max(1+height(root.left),1+height(root.right))
     