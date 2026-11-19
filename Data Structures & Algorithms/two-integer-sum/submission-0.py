class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for i, num in enumerate(nums):
            if target - num in indexMap:
                return [min(i, indexMap[target - num]), max(i, indexMap[target - num])]
            indexMap[num] = i
            
        