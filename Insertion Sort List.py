class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = head
        cur = head.next

        while cur:
            if cur.val >= prev.val:
                prev = cur
                cur = cur.next
            else:
                tmp = dummy
                while tmp.next.val < cur.val:
                    tmp = tmp.next

                prev.next = cur.next
                cur.next = tmp.next
                tmp.next = cur
                cur = prev.next

        return dummy.next
