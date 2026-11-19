class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowK = 1
        uppK = max(piles)
        while lowK < uppK:
            print(lowK)
            midK = (uppK + lowK) // 2
            p = 0
            currH = 0
            while p < len(piles):
                currH += piles[p] // midK
                if piles[p] % midK > 0: 
                    currH += 1
                p += 1
            if currH > h:
                lowK = midK + 1
            if currH <= h:
                uppK = midK


        return lowK



        