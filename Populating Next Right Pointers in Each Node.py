#TC : O(n)
#SC : O(1)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr = root
        nxt = curr.left if curr else None
        while curr and nxt:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
                
            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
                
        return root