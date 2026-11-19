# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        head.next = self.reorder(head.next)

    def reorder(self, head):
        if not head.next:
            return head
        if not head.next.next:
            head.next.next = head
            head = head.next
            head.next.next = None
            return head
        beforeTail = head
        while beforeTail.next.next:
            beforeTail = beforeTail.next
        tail = beforeTail.next
        beforeTail.next = None
        tail.next = head
        head = tail
        head.next.next = self.reorder(head.next.next)
        return head

        