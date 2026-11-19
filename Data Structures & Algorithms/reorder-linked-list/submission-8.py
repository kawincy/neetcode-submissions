# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #put slow right before reversed
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse right half
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge lists
        forward, rev = head, prev
        while forward and rev:
            old = forward
            forward = forward.next
            old.next = rev

            # if rev:
            old = rev
            rev = rev.next
            old.next = forward

        