class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        final = len(prices) - 1

        current_low = prices[0]
        max_profit = 0

        while start < final:

            current = prices[start+1]
            if current < current_low:
                current_low = current

            current_profit = current - current_low
            if current_profit > max_profit:
                max_profit = current_profit

            start +=1

        return max_profit
