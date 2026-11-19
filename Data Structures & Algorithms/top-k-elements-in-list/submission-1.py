class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            countMap[num] += 1
        for num in countMap:
            count = countMap[num]
            # print(num)
            buckets[count].append(num)
            # print(num)
            # print(count)
            print(buckets)
        output = []
        curr = len(nums) - 1
        while len(output) < k:
            while len(buckets[curr]) == 0:
                curr -=1
            output.extend(buckets[curr])
            curr -= 1
        # print(countMap)
        return output

