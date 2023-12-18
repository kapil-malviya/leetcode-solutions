class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if length is different, t is not an anagram of s
        if len(s) != len(t):
            return False
        
        # dictionaries to store the frequency of character in each string
        freq_s = {}
        freq_t = {}
        
        # populate the frequency dictionary for string s
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
            
        # populate the frequency dictionary for string t
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        
        # return true if the comparision is correct
        return freq_s == freq_t