class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # calculate midpoint of search range
            mid = (left + right) // 2
            
            if nums[mid] == target:
                # if midpoint is target, return its index
                return mid
            
            if nums[left] <= nums[mid]:
                # if left half is soted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1       # for target in left sorted half
                else:
                    left = mid + 1        # for target in right unsorted half
            else:
                # for right half sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1        # for tarrget in right sorted half
                else:
                    right = mid -1        # for target in left unsorted half
                
        # if target not in array
        return -1