# from curses.ascii import SO
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최소값과 최대값 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
    


test_python = Solution()

dap = [7, 1, 5, 3, 6, 4]

test_python.maxProfit(dap)