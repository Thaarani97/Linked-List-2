#TC : O(n)
#SC : O(1)
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 1
        if head == None or head.next == None:
            return head
        temp = head
        while(temp.next != None): #counting the length of linked list
            temp = temp.next
            length+=1
        print(temp)
        
        temp.next = head #making the tail of the linked list to point to head
        t = head
        k = k % length
        
        for _ in range(length-k-1):
            t = t.next
        rotatedList = t.next
        t.next = None # breaking the cycle link of the listed list
        return rotatedList