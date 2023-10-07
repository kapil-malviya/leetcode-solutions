class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # check if n is equal to 1 or n divided by 2 is equal to 1
        if n / 2 == 1 or n == 1:
            return True
        
        # if n is greater than 2 and divisible by 2 recursively call function with n/2
        if n > 2:
            return self.isPowerOfTwo(n/2)
        else:
            # if n is not a power of two return False
            return False