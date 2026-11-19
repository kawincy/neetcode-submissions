class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
        minimum = l
        print(minimum)
        if target == nums[minimum]: return minimum
        if target > nums[-1]:
            l, r = 0, minimum - 1
        else:
            l,r  = minimum, len(nums) - 1

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
            