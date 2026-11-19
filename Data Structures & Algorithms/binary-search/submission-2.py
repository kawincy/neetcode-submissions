class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] > target:
                end = mid -1
                # mid = start + ((end - start) // 2)
            elif nums[mid] < target:
                start = mid + 1
                # mid = start + ((end - start) // 2)
            else:
                return mid
        return -1


    # def search(self, nums: List[int], target: int) -> int:
    #     start = 0
    #     end = len(nums) - 1
    #     while start <= end:
    #         if nums[start + ((end - start) // 2)] > target:
    #             end = start + ((end - start) // 2) - 1
    #         elif nums[start + ((end - start) // 2)] < target:
    #             start = start + ((end - start) // 2) + 1
    #         else:
    #             return start + ((end - start) // 2)
    #     return -1
        
        