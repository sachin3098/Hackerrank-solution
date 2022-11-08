Problem Link:

https://www.hackerrank.com/challenges/tree-top-view/problem?isFullScreen=true

def topView(root):
    
    #create a dictionary 
    d={}
    
    #create function for traveeling
    def traverse(root,key,level):
        if root:
            #key not present in dictionary
            if key not in d:
                d[key]=[root,level]
                
            #key with lesser level
            elif d[key][1]>level:
                d[key]=[root,level]
            
            #traverse to left and right of tree
            traverse(root.left,key-1,level+1)
            traverse(root.right,key+1,level+1)
     
    traverse(root,0,0)
    #print the element in order
    for key in sorted(d):
        print(d[key][0], end=" ")