class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0] #Set the buy value to the first item
        profit = 0 

        for i in range(1, len(prices)): #For the prices not including the set buy value
            if prices[i] < buy: #If the new price is lower than the buy set that to the new buy value
                buy = prices[i]
            elif profit < (prices[i] - buy): #Otherwise check how much profit would be made
                profit = prices[i] - buy #If higher than the current highest set new value
        return profit
