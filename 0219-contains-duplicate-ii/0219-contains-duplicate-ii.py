class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        num_index = {}  # store last index where each number occurred
        
        for i, num in enumerate(nums):
            if num in num_index and i - num_index[num] <= k:
                return True
            num_index[num] = i
            
        return False