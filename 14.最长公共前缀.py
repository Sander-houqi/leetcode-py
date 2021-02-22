#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=staHq739311492
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #水平扫描
        if len(strs)==0:
            return ""

        prefix = strs[0]
        for i in range(1,len(strs)):
            #注意这里的限制条件是！=0 不是==-1，否则索引是0的情形没有考虑
            while(strs[i].find(prefix)!=0):
                prefix = prefix[0:len(prefix)-1]
                if len(prefix)==0:
                    return ""
        
        return prefix
            


# @lc code=end

