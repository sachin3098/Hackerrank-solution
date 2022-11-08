Problem Link:

https://www.hackerrank.com/challenges/tree-preorder-traversal/problem?isFullScreen=true

def preOrder(root):
    #Write your code here
    if root:
        # Traverse root
        print(str(root)+" ", end="")
        # Traverse left
        preOrder(root.left)
        # Traverse right
        preOrder(root.right)
    else:
        return preOrder