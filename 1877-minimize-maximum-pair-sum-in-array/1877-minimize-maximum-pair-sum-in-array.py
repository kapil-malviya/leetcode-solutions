class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        end = len(nums)-1
        
        # initialize max pair sum
        max_sum = 0 
        
        while (start < end ):
            result = nums[start] + nums[end]
            #  update start and end
            start += 1
            end -= 1
            
            # if calculated pair sum is greater than current max_sum update thee max_sum
            if result > max_sum :
                max_sum = result
                
        return max_sum