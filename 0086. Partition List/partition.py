# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        node = ListNode()
        i = head
        j = node
        while i != None:
            if i.val < x:
                j.next = ListNode(i.val)
                j = j.next
            i = i.next
        i = head
        while i != None:
            if i.val >= x:
                j.next = ListNode(i.val)
                j = j.next
            i = i.next
        return node.next