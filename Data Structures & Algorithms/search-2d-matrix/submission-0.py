class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        lower = 0
        upper = len(matrix) * len(matrix[0]) - 1
        while lower <= upper:
            mid = (upper - lower) // 2 + lower
            midr = mid // len(matrix[0])
            midc = mid % len(matrix[0])
            if matrix[midr][midc] == target:
                return True
            if matrix[midr][midc] < target:
                lower = mid + 1
            if matrix[midr][midc] > target:
                upper = mid - 1    
        return False    

        