class Solution:
    def largestOddNumber(self, num: str) -> str:

        # iterate through string from right to left
        for i in range(len(num) - 1, -1, -1):
            
            # if current digit is odd
            if int(num[i]) % 2 == 1:
                
                # return substring from beginning to current position
                return num[:i+1]

        # if no odd digit is found, return empty string
        return ""