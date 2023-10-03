class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num = []
        
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                
                # comparing numbers and adding in num
                if nums[i] == nums[j]:
                    num.append([i,j])
        
        # count of matched num
        return len(num)