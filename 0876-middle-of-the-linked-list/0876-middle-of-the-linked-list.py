# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow and fast pointers to the head of the linked list
        slow = fast = head
        
        # Traverse the linked list using the slow and fast pointers
        while fast and fast.next:
            # Move slow pointer one step at a time
            slow = slow.next
            # Move fast pointer two steps at a time
            fast = fast.next.next
        
        # At this point, the slow pointer is at the middle (or second middle) node
        return slow
