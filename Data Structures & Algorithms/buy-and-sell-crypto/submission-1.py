class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        start = 0
        final = len(prices) - 1

        current_low = prices[0] #7
        profit = [0]

        while start < final:

            current = prices[start+1] #1
            if current < current_low:
                current_low = current

            profit.append(current - current_low)

            start +=1

        profit.sort(reverse=True)    
        return profit[0]
