# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        while i != None:
            if i.next == None:
                break
            print(i.val)
            i.val, i.next.val = i.next.val, i.val
            print(i.val, "c")
            i = i.next.next
        return head