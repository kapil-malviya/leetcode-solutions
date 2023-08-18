class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        # iterate through each no. in array
        for unique_no in nums :
            result ^= unique_no     # XOR the current no. with the result
        
        return result