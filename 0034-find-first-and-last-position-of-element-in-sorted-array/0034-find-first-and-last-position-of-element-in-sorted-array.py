class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # function to find first occurrence of target
        def findFirst(nums, target) :
            left = 0
            right = len(nums) - 1
            
            while left <= right :
                mid = left + (right - left) // 2
                if nums[mid] >= target :
                    right = mid - 1
                else :
                    left = mid + 1
                
            return left
        
        # function to find last occurrence of target
        def findLast(nums, target) :
            left, right = 0, len(nums) - 1
            
            while left <= right :
                mid = left + (right - left) // 2
                if nums[mid] <= target :
                    left = mid + 1
                else : 
                    right = mid - 1
                
            return right
        
        # find first & last occurrence
        first = findFirst(nums, target)
        last = findLast(nums, target)
        
        # check if the target was found atleast once
        if first <= last :
            return [first, last]
        else :
            return [-1, -1]