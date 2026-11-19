class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, back = 0, len(numbers) - 1
        while True:
            sum = numbers[front] + numbers[back]
            if target > sum:
                front += 1
            elif target < sum:
                back -= 1
            else:
                return [front + 1, back + 1]
        