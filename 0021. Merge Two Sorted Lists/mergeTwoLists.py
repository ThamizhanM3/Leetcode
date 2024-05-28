# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2
        head = ListNode()
        k = head
        while i != None and j != None:
            k.next = ListNode()
            k = k.next
            if i.val > j.val:
                k.val = j.val
                j = j.next
            else:
                k.val = i.val
                i = i.next
        if j != None:
            k.next = j
        if i != None:
            k.next = i
        return head.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2
        head = ListNode()
        k = head
        while i != None and j != None:
            k.next = ListNode()
            k = k.next
            if i.val > j.val:
                k.val = j.val
                j = j.next
            else:
                k.val = i.val
                i = i.next
        if j != None:
            k.next = j
        if i != None:
            k.next = i
        return head.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        i = list1
        while i != None:
            a.append(i.val)
            i = i.next
        i = list2
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



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        i = list1
        while i != None:
            a.append(i.val)
            i = i.next
        i = list2
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