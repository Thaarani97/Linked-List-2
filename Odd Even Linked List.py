#TC : O(n)
#SC : O(1)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: #base case to handle if the number of nodes is less than 2 in a linked list
            return head
        oddhead = head # to store odd indexed nodes
        evenhead = head.next # to store even indexed nodes
        odd = head
        even = head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenhead
        return oddhead