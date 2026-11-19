class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1

            while count[s[r]] > 1: #while invalid
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        return result