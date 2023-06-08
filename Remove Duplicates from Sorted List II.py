# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy  # prev starts at the dummy node

        curr = dummy.next  # curr starts at the head of the original list
        while curr and curr.next:
            if curr.val == curr.next.val:  # if the value and the next value are equal
                # to iterate through those that are duplicates
                while curr.next and curr.val == curr.next.val:
                    # moving the current node past the duplicate one at a time
                    curr = curr.next
                # prev.next becomes the current next value
                prev.next = curr.next
            else:
                # if we don't have a duplicate, we move one step forward
                prev = prev.next
            # to keep iterating through the list
            curr = curr.next
        return dummy.next
