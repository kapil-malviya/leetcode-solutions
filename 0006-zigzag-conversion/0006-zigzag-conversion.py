class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # if there is only one numRow or is greater than or equal to len(s) then zigzag pattern is same as the original string
        if numRows == 1 or numRows >= len(s) :
            return s
        
        # initialize list to store each rows character
        result = [''] * numRows
        
        index = 0
        step = 1
        
        for char in s :
            result[index] += char
            
            # direction of movement, top -> bottom(step = 1), bottom -> top(step = -1)
            if index == 0 :
                step = 1
                
            elif index == numRows - 1 :
                step = -1 
            
            # move to next row based on diredction
            index += step
            
        return ''.join(result)