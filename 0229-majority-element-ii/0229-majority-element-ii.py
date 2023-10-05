class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        length = len(nums)/3
        
        # occurrence of elements
        count = {}
        # store output
        result = []
        
        for num in nums:
            # increase count of element
            if num in count.keys():
                count[num] += 1
                
            # add new element
            elif num not in count.keys():
                count[num] = 1
        
        # element having occurrence more than n/3 times in a dictionary
        for key in count.keys():
            if count[key] > length:
                result.append(key)
                
        return result
            