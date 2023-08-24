class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # initialize n*n matrix (0 as number)
        matrix = []
        for _ in range(n) :
            row = [0] * n
            matrix.append(row)
            
        num = 1     # starts from 1
        top = 0
        bottom = n-1
        left = 0
        right = n-1
        
        while num <= n*n :
            for i in range(left, right + 1) :    # from left to right
                matrix[top][i] = num      # at top row and i column index
                num = num + 1
            top = top + 1
            
            for j in range(top, bottom + 1) :    # from top to bottom
                matrix[j][right] = num    # at i row and right column index
                num = num + 1
            right = right - 1
            
            for k in range(right, left-1, -1) :    # from right to left
                matrix[bottom][k] = num    
                num = num + 1
            bottom = bottom - 1
            
            for x in range(bottom, top-1, -1) :    # from left to right again
                matrix[x][left] = num
                num = num + 1
            left = left + 1
            
        return matrix