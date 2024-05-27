# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []
        b = []
        c = []
        i = head
        while i != None:
            a.append(i.val)
            i = i.next
        n = len(a) // k
        m = len(a) % k
        print(m)
        for i in range(n):
            for j in range(k):
                b.append(a[(i*k)+j])
            b = b[::-1]
            for i in b:
                c.append(i)
            b = []
        for i in range(m, 0, -1):
            c.append(a[i*-1])

        l = head
        for i in c:
            l.val = i
            l = l.next
        return head