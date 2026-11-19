class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #prefix first
        output = [1]
        for i, num in enumerate(nums):
            output.append(nums[i] * output [i])
       # print(output)

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
           #print (i)
           output[i] *= postfix
           postfix *= nums[i]
        return output[0:len(nums)]
