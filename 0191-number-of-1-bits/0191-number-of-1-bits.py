class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # return bin(n).count('1')
        
        # count number of '1' bits
        count = 0

        while n:
            
            # increment count if least significant bit is 1
            count += n & 1

            # right shift n to remove least significant bit
            n >>= 1

        return count
