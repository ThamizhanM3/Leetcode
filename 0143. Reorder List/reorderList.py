# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if head == None:
            return None
        prev = None
        cur = head
        forw = cur.next
        while forw != None:
            cur.next = prev
            prev = cur
            cur = forw
            forw = forw.next
        cur.next = prev
        return cur

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return
        slow = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            if fast != None:
                slow = slow.next
        newList = slow.next
        l2 = ListNode(newList.val)
        j = l2
        i = newList.next
        while i != None:
            j.next = ListNode(i.val)
            j = j.next
            i = i.next
        l1 = ListNode(head.val)
        i = head.next
        j = l1
        slow = slow.next
        while i != slow:
            j.next = ListNode(i.val)
            j = j.next
            i = i.next
        l2 = self.reverse(l2)
        i = head
        while l2 != None:
            i.val = l1.val
            i.next.val = l2.val
            l1 = l1.next
            l2 = l2.next
            i = i.next.next
        if i != None and l1 != None:
            i.val = l1.val