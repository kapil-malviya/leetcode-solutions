# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        # Iterate through the list
        while current:
            # Store the next node temporarily
            next_node = current.next
            # Reverse the direction of the pointer
            current.next = prev
            # Move the pointers one step forward
            prev = current
            current = next_node

        # After the loop, 'prev' will be the new head of the reversed list
        return prev
