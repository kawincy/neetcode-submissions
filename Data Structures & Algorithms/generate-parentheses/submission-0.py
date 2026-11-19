class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        openCount = 0
        closeCount = 0
        workingString = ""
        def createStrings(openCount, closeCount, workingString):
            if openCount == closeCount == n:
                result.append(workingString)
                return
            if openCount < n:
                workingString+='('
                createStrings(openCount+1, closeCount, workingString)
                workingString = workingString[:-1]
            if openCount > closeCount:
                workingString+=')'
                createStrings(openCount, closeCount+1, workingString)
                workingString = workingString[:-1]
        createStrings(openCount, closeCount, workingString)
        return result


        