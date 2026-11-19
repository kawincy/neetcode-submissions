class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        while i < len(nums):
            target = -nums[i]
            l = i+1
            r = len(nums) - 1
            while l < r:

                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    r -= 1
            # print("left inner loop")
            i += 1
            while i < len(nums) and  nums[i] == nums[i - 1]:
                i += 1
        return result

