class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0 
        n = len(prices)
        i = 0
        
        while i < n-1 :
            # find minimum or buying point
            while i < n-1 and prices[i] >= prices[i+1]:
                # move to next day, till we find price decrease
                i = i + 1
            buy = prices[i]
            
            # find maximum or selling point
            while i < n-1 and prices[i] <= prices[i + 1]:
                i = i + 1
            sell = prices[i]
            
            profit = sell - buy
            
            max_profit = max_profit + profit
        
        return max_profit