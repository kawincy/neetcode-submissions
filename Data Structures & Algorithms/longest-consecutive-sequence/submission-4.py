class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        output = 0
        for num in nums:
            length = 1
            if num - 1 in numSet:
                
                while num in numSet:
                    num +=1
                    length += 1
            if length > output:
                output = length
        return output           


        