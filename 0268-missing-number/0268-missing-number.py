class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        # calculate expected sum of numbers from 0 to n
        expected_sum = (n * (n + 1)) // 2
        
        # calculate sum 
        actual_sum = 0
        for num in nums:
            actual_sum += num
            
        # return difference
        return expected_sum - actual_sum