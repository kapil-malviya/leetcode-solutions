class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums_set = set(nums)
        
        # for storing missing nums
        missing_nums = []
        
        for num in range(1, len(nums)+1):
            if num not in nums_set:
                missing_nums.append(num)
                
        return missing_nums