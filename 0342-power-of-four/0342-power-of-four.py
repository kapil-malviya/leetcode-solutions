class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        
        log_value = math.log(n)/math.log(4)
        return int(log_value) == log_value
        
    ''' 
        if n<=0:
            return False
        
        while n>1:
            if n%4 != 0:
                return False
            n //= 4
            
        return True
    
    '''
        

    