class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        
        # iterate through each character in the roman numeral string
        for i in range(len(s)) :
            # check if the value of current character is less than the value of next character
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]] :
                result-=roman[s[i]]
            else :
                result+=roman[s[i]]
        return result