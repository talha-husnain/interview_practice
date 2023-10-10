class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # If there's only one price, no profit can be made
        if not prices or len(prices) == 1:
            return 0
        
        # Initialize the minimum price with the first price
        minPrice = prices[0]
        
        # Initialize the maximum profit to 0
        maxProfit = 0
        
        # Loop through the prices starting from the second price
        for price in prices[1:]:
            # If the current price is less than the minimum price so far, 
            # update the minimum price
            if price < minPrice:
                minPrice = price
            else:
                # Calculate the profit if selling at the current price and 
                # update maxProfit if it's greater than the previous maxProfit
                maxProfit = max(maxProfit, price - minPrice)
        
        return maxProfit
