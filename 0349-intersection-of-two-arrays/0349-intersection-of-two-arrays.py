class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # remove duplicates
        set1 = set(nums1)
        
        result = []
        
        # iterate through nums2 and check common elements
        for num in nums2:
            if num in set1:
                result.append(num)
                set1.remove(num)     # remove element to avoid duplicates
        
        return result