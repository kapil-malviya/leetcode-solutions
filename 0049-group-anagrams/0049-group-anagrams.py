class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dictionary to store anagrams
        dictt = {}
    
        # iterate through each string in list
        for s in strs:
            # sort character of string and use as key
            sorted_s = ''.join(sorted(s))
            
            # using setdefault to either get the existing list or create a new empty list & append current string to list with sorted keys
            dictt.setdefault(sorted_s, []).append(s)
    
        return list(dictt.values())    