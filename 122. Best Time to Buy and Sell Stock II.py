class Solution(object):
    def maxProfit(self, prices):
        return sum( (prices[i] - prices[i-1]) for i,price in enumerate(prices[1:],1) if prices[i] > prices[i-1])
