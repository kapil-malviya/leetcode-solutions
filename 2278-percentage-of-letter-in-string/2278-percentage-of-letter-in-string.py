class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        count = 0
        
        for char in s:
            if char == letter:
                count += 1
                
        # calculate percentage and round down to the nearest whole percent
        percentage = int(count / len(s) * 100)
        
        return percentage