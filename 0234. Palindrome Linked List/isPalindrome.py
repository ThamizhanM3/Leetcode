# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []
        i = head
        while i != None:
            a.append(i.val)
            i = i.next
        return True if a == a[::-1] else False