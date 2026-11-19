class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for char in t:
            tMap[char] = 1 + tMap.get(char, 0)
        bank = tMap.keys()
        needs = len(bank)
        has = 0
        result = (0, len(s) + 1)
        # window is valid when has == needs

        l = 0
        sMap = defaultdict(int)
        for r in range(len(s)):
            # print(s[l:r])
            if s[r] in bank:
                sMap[s[r]] += 1
                if sMap[s[r]] == tMap[s[r]]:
                    has += 1
            
            while has == needs: #window valid
                #try result update
                # print('here')
                if r - l < result[1] - result[0]:
                    result = (l, r)


                if s[l] in bank:
                    sMap[s[l]] -= 1
                    if sMap[s[l]] < tMap[s[l]]:
                        has -= 1
                l += 1

            
        return s[result[0]:result[1] + 1] if result[1] != len(s) + 1 else ""






