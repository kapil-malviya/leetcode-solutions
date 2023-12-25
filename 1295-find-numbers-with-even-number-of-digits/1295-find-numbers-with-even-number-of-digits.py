class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        # helper function to count no of digits in a number
        def count_digits(num):
            count = 0
            while num != 0:
                num //= 10
                count += 1
            return count

        
        count_even_digits = 0

        for num in nums:
            # check if the no of digits is even
            if count_digits(num) % 2 == 0:
                count_even_digits += 1

        return count_even_digits