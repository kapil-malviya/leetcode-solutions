class Solution:
    def largestGoodInteger(self, num: str) -> str:

        max_good_integer = ""

        # iterate through string until third-to-last character
        for i in range(len(num) - 2):
            
            # if three consecutive characters are same
            if num[i] == num[i+1] == num[i+2]:
                
                # extract current good integer
                current_good_integer = num[i:i+3]

                # update max_good_integer
                max_good_integer = max(max_good_integer, current_good_integer)

        return max_good_integer
