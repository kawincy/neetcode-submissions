class Solution:
    def isValid(self, s: str) -> bool:
        charSet = {'(', '[', '{'}
        charMap = {'(':')', '[':']', '{':'}'}
        charStack = []
        for char in s:
            if char in charSet:
                charStack.append(char)
            elif len(charStack) > 0:
                if charMap[charStack.pop()] != char:
                    return False
            else:
                return False
        return len(charStack) == 0