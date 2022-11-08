Problem Link:

https://www.hackerrank.com/challenges/tree-inorder-traversal/problem?isFullScreen=true

def inOrder(root):
    #Write your code here
    if root:
        # Traverse left
        inOrder(root.left)
        # Traverse root
        print(str(root)+" " , end='')
        # Traverse right
        inOrder(root.right)