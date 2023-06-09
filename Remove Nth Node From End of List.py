# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        #to point to the head incase if we need to make adjustment in the head
        dummy=ListNode(0,head)
        #we use two pointers
        slow=head
        fast=head
        #to move the fast pointer to the position
        for i in range(n):
            fast=fast.next
        
        prev=None
        #to move the slow to previous node of nth node       
        while fast :
            prev=slow
            slow=slow.next
            fast=fast.next
        #check if the node to be removed not head
        if prev:
           prev.next=slow.next
        else:
        
            head=slow.next
        return head
