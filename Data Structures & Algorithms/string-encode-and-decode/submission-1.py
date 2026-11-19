class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            result += str(len(string)) + '@' + string
        return result
        
    def decode(self, s: str) -> List[str]:
        result = []
        cP = 0
        aP = 0
        while cP < len(s):
            while s[aP] != '@':
                aP += 1
            count = int(s[cP:aP])
            result.append(s[aP + 1: aP + 1 + count])
            cP = aP + 1 + count
            aP = aP + 1 + count


        return result
