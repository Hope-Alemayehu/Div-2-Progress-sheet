
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        #two pointers even and odd
        odd = head
        even = head.next
        #to not lose even's head
        even_head = even

        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next

        odd.next=even_head
        return head
