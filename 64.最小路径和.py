#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        rows,cols = len(grid), len(grid[0])
        dp = [ [0]*cols for _ in range(rows)]
        # 左上角初始化
        dp[0][0] = grid[0][0]

        for i in range(1,rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1,cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+ grid[i][j]


        return dp[-1][-1]

# @lc code=end

