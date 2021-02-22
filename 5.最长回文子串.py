#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        length = len(s)
        if length < 2:
            return s
        
        #初始化状态矩阵
        dp = [[False for _ in range(length)] for _ in range(length)]
        
        #对角线length为1，一定是回文
        for i in range(length):
            dp[i][i] =True

        start=0
        max_len=1

        for j in range(1,length):
            for i in range(0,j):
                # 两侧相等，[i+1,j-1]区间，边界条件一定小于2，则一定为回文
                if s[i]==s[j]:
                    # 转移方程
                    if j-i<3:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=False

                #  更新最大回文字串
                if dp[i][j]:
                    cur_len = j-i+1
                    if cur_len > max_len:
                        max_len = cur_len
                        start=i
        
        return s[start:start+max_len]

if __name__ == "__main__":
    s = Solution()
    s.longestPalindrome("cbbd")

# @lc code=end

