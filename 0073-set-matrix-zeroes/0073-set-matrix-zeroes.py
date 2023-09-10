class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix :
            return
        
        m = len(matrix)
        n = len(matrix[0])
        
        zero_rows = set()
        zero_columns = set()
        
        # find position of zero
        for i in range(m) :
            for j in range(n) :
                if matrix[i][j] == 0 :
                    zero_rows.add(i)
                    zero_columns.add(j)
                    
        # set rows with zero
        for row in zero_rows :
            for j in range(n) :
                matrix[row][j] = 0
                
        # set column with zero
        for column in zero_columns :
            for i in range(m) :
                matrix[i][column] = 0