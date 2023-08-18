class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0 and n <= 0 :
            raise VlueError("Undefined result for 0^0 or 0^n when n <= 0")
        
        
        result = x ** n
        return result