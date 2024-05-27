# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if head == None:
            return None
        i = head
        c = 1
        while i.next != None:
            i = i.next
            c += 1
        if c == k:
            return head
        i.next = head
        m = c-k-1 if c > k else c-(k%c)-1
        if c == 2:
            m = (k%2)
            print('hi')
        for i in range(m):
            head = head.next
        if c == 2:
            head.next.next = None
            return head
        x = head
        head = head.next
        x.next = None
        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if head == None:
            return None
        i = head
        c = 1
        while i.next != None:
            i = i.next
            c += 1
        if c == k:
            return head
        i.next = head
        m = c-k-1 if c > k else c-(k%c)-1
        if c == 2:
            m = (k%2)
            print('hi')
        print(m)
        for i in range(m):
            head = head.next
        if c == 2:
            head.next.next = None
            return head
        x = head
        head = head.next
        x.next = None
        return head