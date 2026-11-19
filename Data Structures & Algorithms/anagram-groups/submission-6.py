class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map charCounts to words
        # time: O(n*l) where n is num words and l is length of longest word
        # space: O(n) 
        result = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - 97] += 1
            result[tuple(key)].append(word)
        return list(result.values())
        