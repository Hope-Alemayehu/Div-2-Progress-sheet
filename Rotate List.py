# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        length, tail = 1, head

        # Find the length of the linked list and locate the tail node
        while tail.next:
            tail = tail.next
            length += 1

        # Calculate the effective number of rotations since if k>length no need to go through all that we can just use k % length steps
        k = k % length
        
        curr = head
        # Find the new head node after rotation
        for i in range(length - k - 1):
            curr = curr.next
        
        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead
