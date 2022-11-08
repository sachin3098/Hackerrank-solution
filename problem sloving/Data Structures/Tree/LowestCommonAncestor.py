Problem Link:

https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?isFullScreen=true

def lca(root, v1, v2):
    if v1 < v2:
        return _lca(root, v1, v2)
    else:
        return _lca(root, v2, v1)

def _lca(root, v1, v2):
    #Enter your code here
    if root.info >= v1 and root.info <= v2:
        return root
    if root.info <= v1 and root.info <= v2:
        return _lca(root.right, v1, v2)
    else:
        return _lca(root.left, v1, v2)