class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ## solution. each itereration loop through every word in the dict 
        ## and element wise compare with the tail of the string.
        ## if there is a match, dp[s] is true if dp[s-len(word)] is also true



        n = len(s)
        # m = len(wordDict)
        # t = max len((word))
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, (n + 1)):
            curr = i - 1 # current char index is an index behind the dp index
            for word in wordDict:
                length = len(word)
                if curr + 1 < length: # continue if current word is longer than current string
                    continue
                offset = 0
                for j in range(len(word) - 1, -1, -1):
                    if word[j] != s[curr - offset]:
                        break
                    else:
                        offset += 1
                if offset == length: 
                    if dp [i - length]:
                        dp[i] = True
                        break
        print(dp)
        return dp[-1]
                        



        