class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # invariant valid if windowlen - maxCount <= K
        charMap = defaultdict(int)
        l = 0
        result = 0
        for r in range(len(s)):
            charMap[s[r]] += 1
            maxCount = max(charMap.values())

            while r - l + 1 - maxCount > k:
                charMap[s[l]] -= 1
                l += 1
                maxCount = max(charMap.values())

            result = max(result, r - l + 1 )
        return result




