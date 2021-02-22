#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
     def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]

    # def uniquePaths(self, m: int, n: int) -> int:

    #     # 时间复杂度O(mn),空间复杂度O(n)
    #     # 动态规划，原始空间复杂度为O(mn)，好理解一些

    #     dp = [1]*n
    #     for i in range(1,m):
    #         for j in range(1,n):
    #             dp[j] = dp[j]+dp[j-1]
    #     return dp[-1]
# @lc code=end

