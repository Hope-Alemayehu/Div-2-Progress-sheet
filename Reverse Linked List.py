# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create empty list
        prev = None
        # create a pointer that points to the head at first
        cur = head
        # we want to iterate through the list until cur is pointing to null
        while cur:
            # create another pointer so we won't lose the next node to cur
            temp = cur.next
            # actually reversing it and making it point to prev
            cur.next = prev
            #prev value become cur value
            prev=cur
            # reassign cur to the next node so it iterates to the rest of the node
            cur = temp
        
        return prev
