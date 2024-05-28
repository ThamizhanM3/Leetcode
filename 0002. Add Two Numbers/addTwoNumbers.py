# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i, j = l1, l2
        a = 0
        x = i.val + j.val
        opt = ListNode(x % 10)
        a = x // 10
        i = i.next
        j = j.next
        k = opt
        while i != None and j != None:
            x = i.val + j.val + a
            k.next = ListNode(x % 10)
            a = x // 10
            k = k.next
            i = i.next
            j = j.next
        while i != None:
            x = i.val + a
            k.next = ListNode(x % 10)
            a = x // 10
            k = k.next
            i = i.next
        while j != None:
            x = j.val + a
            k.next = ListNode(x % 10)
            a = x // 10
            k = k.next
            j = j.next
        if a > 0:
            k.next = ListNode(a % 10)
        return opt
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ''
        s2 = ''
        i = l1
        j = l2
        while i != None:
            s1 += str(i.val)
            i = i.next
        while j != None:
            s2 += str(j.val)
            j = j.next
        s3 = str(int(s1[::-1]) + int(s2[::-1]))[::-1]
        head = ListNode()
        i = head
        for j in s3[:-1]:
            i.val = int(j)
            i.next = ListNode()
            i = i.next
        i.val = int(s3[-1])
        return head