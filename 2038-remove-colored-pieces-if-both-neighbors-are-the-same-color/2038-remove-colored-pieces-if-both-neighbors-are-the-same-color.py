class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        num = 0
        
        for i in range(1, len(colors) - 1):
            # alice wins
            if colors[i] == 'A' and colors[i-1] == 'A' and colors[i+1] == 'A':
                num = num + 1
            
            # if bob wins, reduce num
            elif colors[i] == 'B' and colors[i-1] == 'B' and colors[i+1] == 'B':
                num = num - 1
                
        if num > 0:
            return True
        else:
            return False