# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a = []
        for j in lists:
            i = j
            while i != None:
                a.append(i.val)
                i = i.next
        a.sort()
        head = None
        i = head
        for j in a:
            newNode = ListNode(j)
            if i == None:
                i = newNode
                head = i
            else:
                i.next = newNode
                i = i.next
        return head