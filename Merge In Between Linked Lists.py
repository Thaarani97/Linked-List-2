#TC : O(n)
#SC : O(1)
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        curr = list1
        curr1 = copy.deepcopy(list1)
        while curr.val != a-1:
            curr = curr.next
        curr.next = list2
            
        while curr1.val != b+1:
            curr1 = curr1.next
        temp = curr1
       
        curr = list1
        while curr.next!=None:
            curr= curr.next
        curr.next = temp
        
        return list1
        