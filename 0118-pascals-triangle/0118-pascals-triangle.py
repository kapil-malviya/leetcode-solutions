class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows <= 0 :
            return []
        
        # initialise triangle with first row
        triangle = [[1]]
        
        for i in range(1, numRows):
            previous_row = triangle[-1]
            new_row = [1]    # first element of each row is always 1
            
            for j in range(1, i):
               new_row.append(previous_row[j - 1] + previous_row[j])
            
            # last element of each row is always 1
            new_row.append(1)
            triangle.append(new_row)
        
        return triangle