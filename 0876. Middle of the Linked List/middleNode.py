# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow if not fast.next else slow.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow if not fast.next else slow.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow if not fast.next else slow.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow if fast.next == None else slow.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow if fast.next == None else slow.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        i = head
        while i != None:
            n += 1
            i = i.next
        n = n//2
        for i in range(n):
            head = head.next
        return head