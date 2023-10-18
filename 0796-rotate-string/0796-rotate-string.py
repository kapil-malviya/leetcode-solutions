class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        # check if the length of the strings are different
        if len(s) != len(goal):
            return False
        
        # create doubled string by concatinating s with itself
        doubled_s = s + s
        
        # check if goal is a substring of doubled s
        return goal in doubled_s