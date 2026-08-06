class Solution:
    def reorderList(self, head):
        if head is None or head.next is None:
            return

        # 1. Find the end of the first half
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 2. Separate and reverse the second half
        second = slow.next
        slow.next = None

        previous = None
        current = second

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        second = previous

        # 3. Merge the two halves alternately
        first = head

        while second is not None:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        