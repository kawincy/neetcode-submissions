# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # dummy = ListNode()
        # count = 0
        # curr = head
        # while curr:
        #     curr = curr.next
        #     count +=1
        # if count % 2 == 1:
        #     dummy.next = head
        #     curr = dummy.next
        # else:
        #     curr = dummy
        if not head.next:
            return
        head.next = self.reorder(head.next)
        #return dummy.next
        
    
    

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



    #     dummy = ListNode()
    #     count = 0
    #     curr = head
    #     while curr:
    #         curr = curr.next
    #         count +=1
    #     if count % 2 == 1:
    #         dummy.next = head
    #         curr = dummy.next
    #     else:
    #         curr = dummy
    #     curr.next = self.reorder(curr.next)
    #     #return dummy.next
        
    
    

    # def reorder(self, head):
    #     if not head.next.next:
    #         head.next.next = head
    #         head = head.next
    #         head.next.next = None
    #         return head
    #     beforeTail = head
    #     while beforeTail.next.next:
    #         beforeTail = beforeTail.next
    #     tail = beforeTail.next
    #     beforeTail.next = None
    #     tail.next = head
    #     head = tail
    #     head.next.next = self.reorder(head.next.next)
    #     return head


        