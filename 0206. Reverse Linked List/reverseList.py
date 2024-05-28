# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = None
        cur = head
        forw = cur.next
        while forw != None:
            cur.next = prev
            prev = cur
            cur = forw
            forw = forw.next
        cur.next = prev
        return cur



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        a = []
        while i != None:
            a.append(i.val)
            i = i.next
        a = a[::-1]
        j = head
        for i in a:
            j.val = i
            j = j.next
        return head