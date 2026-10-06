class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for l in range(len(prices)):
            r = l + 1
            while r < len(prices):
                res = max(res, prices[r] - prices[l])
                r += 1
        return res





        # for l in range(len(prices)):
        #     if r < len(prices):
        #         res = max(res, prices[r] - prices[l])
        #     r += 1
        # return res