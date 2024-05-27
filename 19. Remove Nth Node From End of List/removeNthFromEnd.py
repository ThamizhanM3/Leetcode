# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1:
            return None
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
        if slow == head and fast == None:
            return head.next
        slow.next = slow.next.next
        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1:
            return None
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
        if slow == head and fast == None:
            return head.next
        slow.next = slow.next.next
        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    head = None
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = head
        m = 0
        while i != None:
            m += 1
            i = i.next
        c = m-n+1
        i = head
        print(c)
        # if c == 1 and n == 1:
        #     return None
        # if c == 2 and n == 1:
        #     head.next = None
        # if c == 1 and n == 2:
        #     return head.next
        # if c == 1:
        #     return head.next
        # if m > 2:
        #     for j in range(c-2):
        #         i = i.next
        #     i.next = i.next.next
        # return head

        if c == 1:
            return head.next
        for j in range(c-2):
            i = i.next
        i.next = i.next.next
        return head



class Solution:
    head = None
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = head
        m = 0
        while i != None:
            m += 1
            i = i.next
        c = m-n+1
        i = head
        if c == 1:
            return head.next
        for j in range(c-2):
            i = i.next
        i.next = i.next.next
        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    head = None
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = head
        m = 0
        while i != None:
            m += 1
            i = i.next
        c = m-n+1
        i = head
        print(c)
        # if c == 1 and n == 1:
        #     return None
        # if c == 2 and n == 1:
        #     head.next = None
        # if c == 1 and n == 2:
        #     return head.next
        # if c == 1:
        #     return head.next
        # if m > 2:
        #     for j in range(c-2):
        #         i = i.next
        #     i.next = i.next.next
        # return head

        if c == 1:
            return head.next
        for j in range(c-2):
            i = i.next
        i.next = i.next.next
        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    head = None
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = head
        m = 0
        while i != None:
            m += 1
            i = i.next
        c = m-n+1
        i = head
        print(c)
        if c == 1 and n == 1:
            return None
        if c == 2 and n == 1:
            head.next = None
        if c == 1 and n == 2:
            return head.next
        if c == 1:
            return head.next
        if m > 2:
            for j in range(c-2):
                i = i.next
            i.next = i.next.next
        return head