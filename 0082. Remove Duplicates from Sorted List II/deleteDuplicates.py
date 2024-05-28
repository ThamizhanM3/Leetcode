# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        cur = head
        nxt = head.next
        nh = ListNode()
        x = nh
        c = 0
        while nxt != None:
            if cur.val == nxt.val:
                nxt = nxt.next
                c = 1
            else:
                if c == 0:
                    x.next = ListNode(cur.val)
                    x = x.next
                c = 0
                cur = nxt
                nxt = nxt.next
        if c == 0:
            x.next = ListNode(cur.val)
            x = x.next
        return nh.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        a = []
        while i != None:
            a.append(i.val)
            i = i.next
        a = Counter(a).items()
        nh = ListNode()
        x = nh
        for i, c in a:
            if c == 1:
                x.next = ListNode(i)
                x = x.next
        return nh.next