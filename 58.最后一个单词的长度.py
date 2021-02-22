#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    # python 取巧解法 
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.strip())==0:
            return 0 
        return len(s.split()[-1])

    # 或者比较一般的解法是从后往前遍历，O(n), 不写了。。。

        
# @lc code=end

