class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # sort piles in descending order
        piles.sort(reverse=True)
        
        n = len(piles) // 3
        coins = 0
        
        # pick second maximum in each triplet
        for i in range(1, n * 2, 2):
            coins += piles[i]
            
        return coins