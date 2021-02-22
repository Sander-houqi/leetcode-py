#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # DP
        m, n = len(text1),len(text2)
        dp = [ [0]*(n + 1) for _ in range(m+1)]

        # 状态转移方程
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+ 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        # return dp[-1][-1]
    
        # 打印所有的公共子序列
        def traceback(i,j,s):

            while i >0 and j>0:
                if text1[i-1]== text2[j-1]:
                    s += text1[i-1]
                    i = i-1
                    j = j-1

                else:
                    if dp[i-1][j]> dp[i][j-1]:
                        i = i -1
                    elif dp[i-1][j]< dp[i][j-1]:
                        j = j -1

                    else:
                        traceback(i-1,j,s)
                        traceback(i,j-1,s)
                        return
            print(s[::-1])

        traceback(len(text1),len(text2),"")




if __name__ == "__main__":
    s1 = 'ABCBDAB'
    s2 = 'BDCABA'
    s = Solution()
    dp = s.longestCommonSubsequence(s1,s2)




# @lc code=end

