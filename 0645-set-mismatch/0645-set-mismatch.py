class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        unique_set = set()
        seen_set = set()
        duplicate = 0
        missing = 0
        
        for num in nums:
            if num not in seen_set:
                seen_set.add(num)
            else:
                duplicate = num
            
            unique_set.add(num)
            
        for i in range(1, n + 1):
            if i not in unique_set:
                missing = i
                break
                
        return [duplicate, missing]