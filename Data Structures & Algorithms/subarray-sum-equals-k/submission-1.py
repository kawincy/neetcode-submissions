class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sum of subarray[m,n] = sum[1,n] - sum[1,m-1] = k

        sumMap = defaultdict(int)
        sumMap[0] = 1
        sm = 0
        result = 0
        for num in nums:
            sm += num
            target = sm - k
            result += sumMap[target]
            sumMap[sm] += 1

            # print(sumMap)
            # print(result)
            # print(sm)

        return result

