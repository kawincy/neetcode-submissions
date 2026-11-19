class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for number in nums:
            countMap[number] = 1 + countMap.get(number, 0)
        freqList = [[] for i in range(len(nums) + 1)]
        for n, c in countMap.items():
            print(c)
            print(n)
            freqList[c].append(n)
        
        result = []
        for i in range(len(freqList)-1, 0, -1):
            for num in (freqList[i]): 
                result.append(num)
                if len(result) >= k:
                    return result


        