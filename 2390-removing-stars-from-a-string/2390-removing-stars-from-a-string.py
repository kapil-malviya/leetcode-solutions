class Solution:
    def removeStars(self, s: str) -> str:
        
        result = []
        i = 0
        
        while i < len(s):
            if s[i] == '*':
                # remove character before the * & skip the *
                if result:
                    result.pop()
                i += 1
            else:
                result.append(s[i])
                i += 1
                
        return ''.join(result)