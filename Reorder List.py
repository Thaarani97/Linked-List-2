#TC : O(n+m)
#SC : O(1)
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        mid = self.findMid(head)
        midnext = mid.next
        mid.next = None
        head1 =  head
        head2 = self.reverse(midnext)
        return self.merge(head1,head2)
       
              
    def findMid(self,head):
        slow = head
        fast = head
        while fast!= None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next 
        return slow
    
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp  
        return prev
    
    def merge(self,head1,head2):
        p1 = head1
        p2 = head2
        while p2:
            temp = p1.next
            p1.next = p2
            p2=p2.next
            p1.next.next=temp
            p1 = temp   
        return head1
        
            
            