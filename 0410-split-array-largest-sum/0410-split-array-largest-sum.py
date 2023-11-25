class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # function to count the number of subarrays with sum less than or equal to max_sum
        def count_groups(nums, max_sum):
            count = 1
            current_sum = 0

            for num in nums:
                current_sum += num
                if current_sum > max_sum:
                    count += 1
                    current_sum = num

            return count

        
        # initializee search range
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            groups = count_groups(nums, mid)

            if groups > k:          # if no. of groups is more than k, adjust search range to right
                left = mid + 1          
            else:                   # if less than or equal to k, adjust search range to left
                right = mid

        return left