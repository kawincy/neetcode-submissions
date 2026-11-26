"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        converter = {}
        copyhead = Node(head.val)

        converter[head] = copyhead
        converter[None] = None


        copycurr = copyhead

        curr = head.next
        while curr:
            copycurr.next = Node(curr.val)
            copycurr = copycurr.next

            converter[curr] = copycurr

            curr = curr.next
        


        curr = head
        copycurr = copyhead


        while curr:
            copycurr.random = converter[curr.random]
            curr = curr.next
            copycurr = copycurr.next

        return copyhead