# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # to extract the values from the linked list and store them in nodevalue
        nodevalue = []
        current = head
        while current:
            nodevalue.append(current.val)
            current = current.next
        
        # to Initialize an output list with zeros, which will be updated with the next greater elements
        output = [0] * len(nodevalue)

        # we use a stack to keep track of indices in nodevalue
        stack = []
        
        # to iterate through nodevalue and find the next greater element for each value
        for index, value in enumerate(nodevalue):
            # while the stack is not empty and the value is greater than the element at the top of the stack,
            # update the output with the value and remove the index from the stack
            while stack and nodevalue[stack[-1]] < value:
                output[stack.pop()] = value
            
            # push the current index onto the stack
            stack.append(index)
        
        # return the final output list
        return output
