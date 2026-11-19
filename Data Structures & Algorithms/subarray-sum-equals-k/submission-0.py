class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int) #values -> num prefixes with that value
        total = 0
        prefixes[0] = 1

        result = 0
        for n in nums:
            total += n
            result += prefixes[total - k]
            prefixes[total] += 1
        return result 