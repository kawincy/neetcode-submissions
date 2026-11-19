class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1

        while l + 1  < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid
                # if nums[l+1] > nums[l]:
                #     l += 1
            if nums[mid] < nums[r]:
                r = mid
                if nums[r-1] < nums[r]:
                    r -= 1
        return nums[r]
        