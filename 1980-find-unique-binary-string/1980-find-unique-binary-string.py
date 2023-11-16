class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        # create binary string
        ones = "1" * n
        zeros = "0" * n

        # check binary string of all zeros is not in nums
        if zeros not in nums:
            return zeros

        # check binary string of all ones is not in nums
        if ones not in nums:
            return ones
        
        for binary_str in nums:
            if binary_str[::-1] not in nums:
                return binary_str[::-1]
        
        return "10"