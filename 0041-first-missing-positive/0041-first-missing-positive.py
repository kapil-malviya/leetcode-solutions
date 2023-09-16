class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
    
   
        '''
        i = 1
        while i in nums:
            i += 1
        return i
        
    sets have an average time complexity of O(1) for this operation, 
    while lists have a time complexity of O(n) for linear searches.'''
    
    
    
        i = 1
        nums = set(nums)
        while i in nums:
            i += 1
        return i 
        
    