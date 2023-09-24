class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # initializing 1 to increment value by 1
        carry = 1
        n = len(digits)
        
        # iterate through the digits
        for i in range(n-1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            # calculate carry for next digit
            carry = total // 10
            
        # if there is carry remaining
        if carry:
            # add new digit at the beginning
            digits.insert(0, carry)
            
        return digits