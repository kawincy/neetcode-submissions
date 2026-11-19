# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            

        # if not head.next:
        #     return head
        # if not head.next.next:
        #     head.next.next = head
        #     head = head.next
        #     head.next.next = None
        #     return head
            
        # pointer2 = head.next.next
        # head.next.next = head
        # head = head.next
        # head.next.next = None
        # pointer3 = pointer2.next

        # while pointer3.next:
        #     pointer2.next = head
        #     head = pointer2
        #     pointer2 = pointer3
        #     pointer3 = pointer2.next
        
        # pointer2.next = head
        # pointer3.next = pointer2
        # return pointer3

        