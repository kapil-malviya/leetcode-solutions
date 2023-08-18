class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    
        reversed_x = 0
        original_x = x
    
        while x > 0:
            digit = x % 10                          # get last digit of x variable
            reversed_x = reversed_x * 10 + digit    # add digit to reversed_x variable
            x = x // 10                       # remove last digit from x
    
        return original_x == reversed_x