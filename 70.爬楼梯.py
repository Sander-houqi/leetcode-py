#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:

    # 动态规划
    # 分解为最优子结构的子问题。f(n)=f(n-1)+f(n-2)
    def climbStairs(self, n: int) -> int:
        if n==1:
            return n
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        # range 左闭右开
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[n]

    # 斐波那契数列，递归(时间复杂度高)，用迭代法
    # def climbStairs(self,n):
    #     if n==1:
    #         return 1

    #     a = 1
    #     b = 1
    #     # for _ in range(2,n+1):
    #     #     c = a+b
    #     #     a = b
    #     #     b = c
    #     # return c

    #     for _ in range(2,n+1):
    #         # 可以简化为
    #         a , b = b, a+b

    #     return b
    
    # 递归会超时间
    # def climbStairs(self,n):
    #     if n<=1:
    #         return 1
    #     return self.climbStairs(n-1)+self.climbStairs(n-2)

        
    



# @lc code=end

