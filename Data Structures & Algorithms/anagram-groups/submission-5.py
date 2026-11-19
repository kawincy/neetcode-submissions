class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            key = [0 for _ in range(26)]
            for char in word:
                key[ord(char) - 97] += 1
            result.setdefault(tuple(key), []).append(word)
        return list(result.values())
        