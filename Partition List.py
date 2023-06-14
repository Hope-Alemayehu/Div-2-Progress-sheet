# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #sub lists to store the ordered lsit
        left=ListNode()
        right=ListNode()
        
        #always point to the last node in the left and right list
        lefttail=left
        righttail= right

    #adding elements to the sublist
        while head:
            if head.val<x:
                lefttail.next=head
                lefttail=lefttail.next
            else:
                righttail.next=head
                righttail=righttail.next
            head=head.next
        #connect the sub list
        lefttail.next=right.next
        righttail.next= None

        return left.next




