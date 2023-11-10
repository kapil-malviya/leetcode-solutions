class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        new_nums = []
        mid = n
        
        for number in range(n):   
            # append element from first half of nums to new_nums
            new_nums.append(nums[number])
            
            # append element from second half of nums to new_nums
            new_nums.append(nums[mid])
            
            mid += 1
            
        return new_nums