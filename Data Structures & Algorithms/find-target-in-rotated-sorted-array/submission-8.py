class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            elif nums[mid] < nums[-1]:
                r = mid
            # else: #this should only hit if l == r == nums[-1] which won't happen
            #     pass

        minInd= l

        if target > nums[-1]:
            l, r = 0, minInd - 1
        else:
            l, r = minInd, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else: #this should only hit if l == r == nums[-1] which won't happen
                return mid
        return -1
        
