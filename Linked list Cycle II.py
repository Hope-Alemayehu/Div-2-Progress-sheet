# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            #checks if the cycle exists
            if fast == slow:
                #to iterate through the list again to find where the cycle start
                slow2 = head
                
                while slow2 != slow:
                    slow = slow.next
                    slow2 = slow2.next
                #return where they meet
                return slow
        
        return None
