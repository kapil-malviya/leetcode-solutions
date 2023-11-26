class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        j = 0      # pointer to keep track of the position for next non-zero element
        
        # iterate through the array
        for i in range(len(nums)):
            # if current element is non-zero, move it to next non-zero position
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1