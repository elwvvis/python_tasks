class Solution(object):
    def maxProfit(self, prices):
        profit = 0 
        minCost = prices[0]
        for price in prices:
            net_profit = price - minCost

            if net_profit > profit:
                profit = net_profit

            if price < minCost:
                minCost = price

        return profit