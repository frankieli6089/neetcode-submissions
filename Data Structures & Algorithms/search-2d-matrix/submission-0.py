class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * (len(matrix[0])) - 1
        
        while low <= high:
            mid = ((high - low) // 2) + low
            row_idx = mid // cols
            col_idx = mid % cols
            if matrix[row_idx][col_idx] < target:
                low = mid + 1
            elif matrix[row_idx][col_idx] > target:
                high = mid - 1
            elif matrix[row_idx][col_idx] == target:
                return True
        
        return False
