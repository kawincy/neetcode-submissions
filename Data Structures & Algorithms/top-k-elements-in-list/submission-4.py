class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        buckets = [[] for _ in range(len(nums))]
        for num, count in counts.items():
            buckets[count-1].append(num)

        flattened = []
        for bucket in buckets:
            if bucket:
                flattened += bucket
        return flattened[-k:]