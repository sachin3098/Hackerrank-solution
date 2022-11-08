Problem Link:

https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?isFullScreen=true

def findMergeNode(head1, head2):
    
    def getcount(head):
        n=0
        while head.next!=None:
            head=head.next
            n+=1
        return n
    
    #def get common node
    def getnode(d,head1,head2):
        #traverse upto d
        for i in range(d):
            head1=head1.next
            
    #check the common node
        while head1 and head2:
            if head1==head2:
                return head1.data
            else:
                head1=head1.next
                head2=head2.next
                
        
    c1=getcount(head1)
    c2=getcount(head2)
    
    #check difference
    if c1>c2:
        return getnode(c1-c2,head1,head2)
    else:
        return getnode(c2-c1,head2,head1)