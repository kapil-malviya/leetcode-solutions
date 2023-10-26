class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        left = self.sortArray(left)
        right = self.sortArray(right)
        
        return self.sortedNums(left, right)
    
    
    def sortedNums(self, a, b):
        
        len_a = len(a)
        len_b = len(b)
        
        i = j = 0
        
        merged = []
        
        while i < len_a and j < len_b:
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
                
            else:
                merged.append(b[j])
                j += 1
            
        merged.extend(a[i:])
        merged.extend(b[j:])
        
        return merged