class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        
        # calculate the sum of the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        for i in range(k, n):
            current_sum = current_sum + nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
        
        # calculate max average
        max_average = max_sum / k
        
        return max_average