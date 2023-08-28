class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right :
            # calculate the middle index
            mid = left + (right - left) // 2
            
            if nums[mid] == target :
                return mid      # if found target, return index
            elif nums[mid] < target :
                left = mid + 1
            else : 
                right = mid - 1
                
        return left