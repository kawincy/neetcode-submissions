# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arrayList = []
        curr = head
        while curr:
            arrayList.append(curr)
            curr = curr.next
        if n + 1 > len(arrayList):
            head = head.next
            # return head
        else:
            print(arrayList[-(n + 1)].val, arrayList[-n].val)
            arrayList[-(n + 1)].next = arrayList[-n].next
        return head
        