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

        if not head:
            return None

        deepCopies = [Node(head.val)]
        curr = head.next

        copyPairs = {None : None, head: deepCopies[0]}

        while curr:
            deepCopies.append( Node(curr.val) )
            deepCopies[-2].next = deepCopies[-1]
            copyPairs[curr] = deepCopies[-1]
            curr = curr.next

        curr = head
        count = 0
        while curr:
            # print(count, curr, deepCopies[count-1].random)
            deepCopies[count].random = copyPairs[curr.random]
            curr = curr.next
            count += 1

        return deepCopies[0]
        

        # deepCopies = [] #indexable container for listnodes
        # values = [] # will contain the value of each node at each corresponding index
        # indMap = {None : None}


        # while head:
        #     newNode = Node(head.val) 
        #     if head.next:
        #         newNode.next = head.next.val
        #     else:
        #         newNode.next = None

        #     if head.random:
        #         newNode.random = head.random.val
        #     else:
        #        newNode.random = None

        #     deepCopies.append(newNode)
        #     values.append[head.val]
        #     indMap[head.val] = len(deepCopies) - 1

        #     head = head.next
        
        

        # for ind, element in enumerate(deepCopies):
        #     if element.next:
        #         element.next = deepCopies[indMap[element.next]]
        #     if element.random:
        #         element.random = deepCopies[indMap[element.random]]

        # return deepCopies[0]
        