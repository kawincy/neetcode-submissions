class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # prefix loop
        pre = nums[0]
        pointer = 1
        while pointer < len(nums):
            output[pointer] *= pre
            pre *= nums[pointer]
            pointer += 1
        print(output)
        # output loop
        post = nums[-1]
        pointer = len(nums) - 2
        while pointer > -1:
            output[pointer] *= post
            post *= nums[pointer]
            pointer -= 1

        return output

            



        # post fix loop