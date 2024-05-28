# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        i = head
        a = []
        while i != None:
            a.append(i.val)
            i = i.next
        a.sort()
        i = head
        j = 0
        while i != None:
            i.val = a[j]
            j += 1
            i = i.next
        return head