# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        if head.val == val:
            head = head.next
            return self.removeElements(head, val)
        i = head
        while i != None and i.next != None:
            if i.next.val == val:
                i.next = i.next.next
                return self.removeElements(head, val)
            i = i.next
        return head