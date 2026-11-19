class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maptolist = {}
        for word in strs:
            # print('1')
            letters = [0 for _ in range(26)]
            for char in word:
                letters[ord(char) - 97] += 1
            # print(maptolist)
            maptolist.setdefault(tuple(letters), []).append(word)
            # print('2')
        result = list(maptolist.values())
        return result
