class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window if valid if window len - maxCount <= k
        # intialize map
        charMap = defaultdict(int)
        #initialize pointers
        l, r = 0, 0
        # init map with first char
        charMap[s[l]] += 1

        result = 0
        # slide window
        while r < len(s):
            #find max count
            maxCount = 0
            for char in charMap:
                maxCount = max(maxCount, charMap[char])
            #determine validity
            if r - l + 1 - maxCount <= k:
                result = max(result, r - l + 1)
                r += 1
                if r < len(s):
                    charMap[s[r]] += 1
            else:
                charMap[s[l]] -= 1
                l += 1
        return result
