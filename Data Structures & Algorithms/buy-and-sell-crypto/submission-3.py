class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        sell_index = 1
        max_profit = 0
        min_buy = float('inf')

        while sell_index < len(prices):
            if prices[sell_index] - prices[buy_index] < 0:
                buy_index = sell_index
                sell_index += 1
            elif prices[sell_index] - prices[buy_index] <= max_profit:
                sell_index += 1
            
            elif prices[sell_index] - prices[buy_index] > max_profit:
                max_profit = prices[sell_index] - prices[buy_index]
                sell_index += 1
        
        return max_profit