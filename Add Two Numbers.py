#TC : O(n)
#SC : O(1)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr1 = l1
        curr2 = l2
        sumval = 0
        carrier = 0
        dummy = ListNode(-1,-1)
        head = dummy
        while curr1 or curr2 or carrier:
            l1val = curr1.val if curr1 else 0 
            l2val = curr2.val if curr2 else 0
            sumval = l1val + l2val + carrier
            carrier = sumval//10
            dummy.next=ListNode(sumval%10)
            dummy = dummy.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        return head.next
            