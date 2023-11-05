class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        current_winner = arr[0]
        win_count = 0
        
        for i in range(1, n):
            if arr[i] > current_winner:
                current_winner = arr[i]
                win_count = 1
            else:
                win_count += 1
                
            if win_count == k:
                return current_winner
        
        return current_winner