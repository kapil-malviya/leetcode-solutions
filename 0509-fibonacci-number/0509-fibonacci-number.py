class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        elif n == 1 :
            return 1
        
        else:
            # variables to store previous two fibonacci numbers
            num1 = 0
            num2 = 1
            
            for _ in range(2, n+1):
                # calculate next fibonacci no. and update
                num1, num2 = num2, num1 + num2
                
            return num2