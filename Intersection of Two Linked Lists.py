#TC : O(n)
#SC : O(1)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        lenA = 0
        lenB = 0
        
        while p1:
            p1 = p1.next
            lenA+=1
        while p2:
            p2 = p2.next
            lenB+=1
            
        p1 = headA
        p2 = headB
        
        while lenA>lenB:
            p1 = p1.next
            lenA-=1
        while lenB>lenA:
            p2 = p2.next
            lenB-=1
        
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
            