#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# @lc code=start

"""
数组越界
正负数
010 特殊情况
##python除整取余数带尝试（python的取余是向下）
"""
class Solution:
    def reverse(self, x: int) -> int:
        num = x
        reverse_int = 0
        if num<0:
            num  = str(num)[1:]
            reverse_int= -1*int(num[::-1])
        else:
            #int("012") -->12
            reverse_int= int(str(num)[::-1])

        if -2**31 <= reverse_int <= 2**31-1:
            return reverse_int
        else:
            return 0 

    #另外一种解法
    # def reverse(
    #         self, 
    #         x: int) -> int:
            
    #         y, res = abs(x), 0
    #         # 则其数值范围为 [−2^31,  2^31 − 1]
    #         boundry = (1<<31) -1 if x>0 else 1<<31
    #         while y != 0:
    #             res = res*10 +y%10
    #             y //=10
    #         if res > boundry :
    #                 return 0
    #         return res if x >0 else -res


        
# @lc code=end

