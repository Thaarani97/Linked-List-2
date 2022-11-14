#TC : O(n)
#SC : O(1)
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummynode = ListNode(-1)
        dummynode.next = head
        head = dummynode
        firstnode = head.next
        while firstnode and firstnode.next != None:
            secondnode = firstnode.next
            temp = secondnode.next
            secondnode.next = firstnode
            firstnode.next = temp
            dummynode.next = secondnode
            dummynode = firstnode
            firstnode = temp
        
        return head.next