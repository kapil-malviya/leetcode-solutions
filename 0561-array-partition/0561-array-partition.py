class Solution:
    
#     def bubbleSort(self, nums):
#         n = len(nums)
        
#         for i in range(n - 1):
#             for j in range(n - i - 1):
#                 if nums[j] > nums[j + 1]:
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
        
    def arrayPairSum(self, nums: List[int]) -> int:
        
        # self.bubbleSort(nums)
        nums.sort()        
        max_sum = 0
        
        for i in range(0, len(nums), 2):
            max_sum = max_sum + nums[i]
            
        return max_sum