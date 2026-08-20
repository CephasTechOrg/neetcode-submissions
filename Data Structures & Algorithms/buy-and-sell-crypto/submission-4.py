class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying_min_price = prices[0]
        for price in prices:
            if price < buying_min_price:
                buying_min_price = price
            profit = price - buying_min_price
            max_profit = max(max_profit, profit)
        return max_profit