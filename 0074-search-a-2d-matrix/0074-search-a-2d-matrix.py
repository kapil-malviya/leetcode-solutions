class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return false
        
        # no of rows and columns in matrix
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m * n - 1
        
        while left <= right:
            # calculating middle index
            mid = (left + right) // 2
            # middle value
            mid_value = matrix[mid // n][mid % n]
            
            if mid_value == target :
                return True
            
            elif mid_value < target:
                left = mid + 1
            
            else :
                right = mid - 1
                
        return False