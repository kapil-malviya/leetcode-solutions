class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # creating copy of list
        nums[:] = sorted(set(nums))  
        return len(nums)