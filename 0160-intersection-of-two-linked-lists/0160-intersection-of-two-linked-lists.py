# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        # Length of nodes
        lenA = getLength(headA)
        lenB = getLength(headB)
        
        # Set pointers to heads
        p1 = headA
        p2 = headB
        
        # Move pointer of the longer list ahead
        while lenA > lenB:
            p1 = p1.next
            lenA -= 1
        while lenB > lenA:
            p2 = p2.next
            lenB -= 1
        
        # Move both pointers until they meet
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        # p1 or p2 is intersection point (or None if no intersection)
        return p1
