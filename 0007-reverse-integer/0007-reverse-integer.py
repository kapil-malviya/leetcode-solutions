class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0 :
            # convert int to string and with the help of slicing reverse the string
            reversed_x = int(str(x)[::-1])          
        else :
            reversed_x = -int(str(-x)[::-1])
            
        if reversed_x < -2**31 or reversed_x > 2**31 - 1 :
            return 0
            
        return reversed_x