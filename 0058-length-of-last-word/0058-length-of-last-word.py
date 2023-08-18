class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        trimmed_s = s.strip()         # removing spaces at the begining   
        words = trimmed_s.split()     # split words using spaces
        last_word = words[-1]         # find last word
        return len(last_word)         # length of last word