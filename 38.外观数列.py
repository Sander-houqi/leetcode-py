# -*- coding: utf-8 -*-
#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    # def countAndSay(self, n: int) -> str:
    #     # 没想到什么好的思路，直接遍历吧
        
    #     s = "1"
    #     for i in range(n-1):
    #         #初始化相关变量
    #         char = s[0]
    #         count = 0
    #         tmp = ''
    #         for j in s:
    #             if char == j:
    #                 count += 1
    #             else:
    #                 tmp = tmp+ str(count)+char
    #                 count = 1
    #                 char = j
    #         # 别忘记了
    #         tmp = tmp+str(count)+char
    #         s = tmp

    #     return s


    #递归(参考的，递归debug更好理解）
    def countAndSay(self, n: int) -> str:
        if n<=1: return "1"
        num = self.countAndSay(n-1)+"*"
        print(num)
        temp = list(num)
        count = 1
        strBulider = ''
        # print(len(temp))
        for i in range(len(temp)-1):
            if  temp[i] == temp[i+1] :
                    count += 1  
            else:
                if temp[i] != temp[i+1]:
                    strBulider +=  str(count) + temp[i]
                    count = 1
        return strBulider


        
# @lc code=end

if __name__ == "__main__":
    S= Solution()
    print(S.countAndSay(4))