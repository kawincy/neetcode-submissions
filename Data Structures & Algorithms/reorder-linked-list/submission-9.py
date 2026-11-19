# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow
        slow = slow.next
        temp.next = None

        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp

        while head and prev:

            htemp = head
            head = head.next
            htemp.next = prev
            
            ptemp = prev
            prev = prev.next
            ptemp.next = head

            # print(head.val)
            # print(prev.val)
            # break


