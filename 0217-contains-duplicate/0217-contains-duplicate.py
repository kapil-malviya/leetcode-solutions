class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # create dictionary to store values
        dictt = {}
        
        for num in nums:
            if num in dictt:
                # if no. already in dictionary, it is duplicate
                return True
            else:
                dictt[num] = 1   # add no. to dict
        
        # if loop completes without finding any duplicates
        return False