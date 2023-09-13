class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        medium = 0
        high = len(nums) - 1
        
        while medium <= high :
            # if current element is red
            if nums[medium] == 0 :
                # swaping the elements
                nums[low], nums[medium] = nums[medium], nums[low]
                # move low and medium pointers forward
                low = low + 1
                medium = medium + 1
                
            # if current element is white
            elif nums[medium] == 1 :
                # move medium pointer forward
                medium = medium + 1
                
            # if element is blue
            else :
                # swap current element with element at high position
                nums[medium], nums[high] = nums[high], nums[medium]
                # move pointer backward
                high = high - 1
                
        return nums