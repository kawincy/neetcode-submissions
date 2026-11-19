import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+','-','*','/'}
        stack = []
        for item in tokens:
            if item not in operators:
                stack.append(int(item))
            elif item == '+':
                stack.append(stack.pop() + stack.pop())
            elif item == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            elif item == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                #stack.append(op1 // op2 if op1 // op2 >= 0 else op1 // op2 + 1 )
                stack.append(math.trunc(op1/op2))
        return stack.pop()
            