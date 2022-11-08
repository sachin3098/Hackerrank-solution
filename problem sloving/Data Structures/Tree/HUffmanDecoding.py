problem Link:

https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?isFullScreen=true

def decodeHuff(root: Node, s: str):
    node = root
    traversing: bool = True
    for c in s:
        if c == "1":
            node = node.right
        else:
            node = node.left
        if node.data != "\0":
            print(node.data, end="")
            node = root