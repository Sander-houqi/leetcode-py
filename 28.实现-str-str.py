#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

"""双指针遍历
    复杂点的话就是KMP算法，以后在看"""
# @lc code=start
class Solution:
    # 遍历的时候一定要考虑最后的遍历停止条件，才能AC
    # def strStr(self, haystack: str, needle: str) -> int:
    #     if needle=="":
    #          return 0
        
    #     # 这里是关键，一定要减去要搜索的字符串的长度。要不会超时
    #     for i in range(len(haystack)-len(needle)+1):
    #         s_i=i
        
    #         for j in range(len(needle)):
    #             if s_i<len(haystack) and haystack[s_i]==needle[j]:
    #                 s_i = s_i + 1
    #             else:
    #                 break
    #         if s_i-i == len(needle):
    #             return i
                    
    #     return -1


    # python find
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle) if needle in haystack else -1

        
# @lc code=end

