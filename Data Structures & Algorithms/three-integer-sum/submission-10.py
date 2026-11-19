class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-2):
            if i != 0 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = len(nums) - 1
            target = -nums[i]

            while l < r:
                total = nums[l] + nums[r]

                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
        return result

            
 
