# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(0)
        #to start of the sum 
        cur=dummy
        #intalizing carry for further calculation
        carry=0

        #this loop stops only if all the carry,l1,l2 are null
        while carry or l1 or l2:
            if l1:
               carry+=l1.val
               l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            #since the nodes only store single digit we use this 
            cur.next=ListNode(carry%10)
            #to pass the carry if any.for example if carry=5 then here the carry 5//10 = 0
            #Example: if carry =12 here carry becomes 12//10 = 1 this would be passed for next iteration
            carry//=10
            #to move the cur pointer to next because we need it as a chain if its not there it would only print the last iteration result.
            cur=cur.next
        return dummy.next

