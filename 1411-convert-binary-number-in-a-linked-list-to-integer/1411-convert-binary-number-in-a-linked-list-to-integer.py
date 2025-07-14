# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        current = head 
        binary_string = ""
        while current:
            binary_string += str(current.val)
            current = current.next
        return int(binary_string,2)
        