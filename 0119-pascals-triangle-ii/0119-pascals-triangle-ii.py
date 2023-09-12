class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex < 0:
            return []
        
        # initialize first row with 1
        current_row = [1]
        
        for i in range(1, rowIndex + 1):
            # create new row, starts from 1
            new_row = [1]
            
            # calculate middle element by adding no from previous row
            for j in range(1, len(current_row)):
                new_row.append(current_row[j - 1] + current_row[j])
                
            # add last element as 1
            new_row.append(1)
            
            current_row = new_row
            
        return current_row