class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_stock=float("inf")
        for i in prices:
            min_stock=min(min_stock,i)
            max_profit=max(i-min_stock,max_profit)
        return max_profit
        