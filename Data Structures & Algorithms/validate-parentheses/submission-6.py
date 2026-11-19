class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' \
            or c == '{' \
            or c == '[':
                stack.append(c)
            elif not stack or abs(ord(c) - ord(stack[-1])) > 2: #uses ascii values
                return False
            else:
                # print(ord(c) - ord(stack[-1]))
                stack.pop()
                

        
        return not stack

        