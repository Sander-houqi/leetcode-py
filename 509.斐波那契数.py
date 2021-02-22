#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    # 动态规划
    def fib(self, N: int) -> int:
        if N<=1:
            return N
            
        dp = [0]*(N)
        dp[0]= dp[1]=1
        for i in range(2,N):
            dp[i]= dp[i-1]+dp[i-2]

        return dp[-1]


# @lc code=end

