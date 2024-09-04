# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        i = head
        opt = []
        n = 0
        while i != None:
            n += 1
            i = i.next
        x = n % k
        s = n // k
        qw = head
        for i in range(k):
            z = 1 if x > 0 else 0
            x -= 1
            ol = ListNode()
            nl = ol
            for j in range(s+z):
                if qw != None:
                    nl.next = ListNode(qw.val)
                    qw = qw.next
                    nl = nl.next
            opt.append(ol.next)
        # for i in opt:
        #     j = i
        #     while j != None:
        #         print(j.val, end = " ")
        #         j = j.next
        #     print()
        return opt