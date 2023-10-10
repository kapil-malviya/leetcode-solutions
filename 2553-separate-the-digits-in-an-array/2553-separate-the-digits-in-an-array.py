class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        result = []
        
        for num in nums:
            num_string = str(num)
            
            for char in num_string:
                digit = int(char)
                result.append(digit)
                
        return result