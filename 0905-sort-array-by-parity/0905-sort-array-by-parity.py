class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:    
        even_nums = [x for x in nums if x % 2 == 0]
        odd_nums = [x for x in nums if x % 2 != 0 ]
        return even_nums + odd_nums