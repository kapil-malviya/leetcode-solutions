class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        
        log_value = math.log10(n)/math.log10(3)
        return int(log_value) == log_value