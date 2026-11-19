# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        curr = head
        print(curr)
        print(head)

        while list1 and list2:
            # print('here')
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        print("made it")
        if list1:
            curr.next = list1
            return head
        curr.next = list2
        return head

        # if not list1:
        #     return list2
        # if not list2:
        #     return list1

        # # Initialize a dummy node to simplify the linking process
        # dummy = ListNode(0)
        # curr = dummy

        # # Traverse both lists and merge them
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         curr.next = list1  # Directly link to the smaller node
        #         list1 = list1.next
        #     else:
        #         curr.next = list2  # Directly link to the smaller node
        #         list2 = list2.next
        #     curr = curr.next

        # # At the end, link the remaining nodes from the non-empty list
        # if list1:
        #     curr.next = list1
        # else:
        #     curr.next = list2

        # # Return the merged list, which starts from dummy.next
        # return dummy.next



        