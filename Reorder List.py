#TC : O(n+m)
#SC : O(1)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.findMid(head)
        mid_next = mid.next
        mid.next = None
        head1 = head
        head2 = self.reverse(mid_next)
        return self.merge(head1,head2)     
    
    def findMid(self,head):
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        
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