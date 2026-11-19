class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):
          #  if stack:
            for i in range(len(stack)):
                if temp > stack[-1][1]: 
                    oldDay = stack.pop()
                    output[oldDay[0]] += day - oldDay[0]
                else:
                    break
            stack.append((day, temp))
        return output
