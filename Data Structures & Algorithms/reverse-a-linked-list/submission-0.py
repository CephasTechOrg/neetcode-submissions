class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        current = head
        
        while current:
            next_node = current.next   # save next node
            current.next = prev        # reverse pointer
            
            prev = current             # move prev forward
            current = next_node        # move current forward
        
        return prev
