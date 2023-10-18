class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ensure k is in range of array length
        k = k % len(nums)
        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        n = len(nums)
        
        reverse(0, n-1)         # reverse entire array
        reverse(0, k-1)         # reverse first k elements
        reverse(k, n-1)         # reverse remaining elements