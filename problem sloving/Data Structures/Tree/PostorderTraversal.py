Problem Link:

https://www.hackerrank.com/challenges/tree-postorder-traversal/problem?isFullScreen=true

def postOrder(root):
    #Write your code here
    if root:
        # Traverse left
        postOrder(root.left)
        # Traverse right
        postOrder(root.right)
        # Traverse root
        print(str(root)+" ", end='')