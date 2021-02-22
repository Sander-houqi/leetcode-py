#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

"""leetcode 官方题解反转一半数字亦可"""
# @lc code=start
class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     str_x = str(x)
    #     str_reverse = str_x[::-1]
    #     if str_x ==str_reverse:
    #         return True
    #     else:
    #         return False

    # 方法二: 将int转化成str类型: 双指针 (指针的性能一直都挺高的)
    # 复杂度: O(n)
    def isPalindrome(self, x: int) -> bool:
        lst = list(str(x))
        L, R = 0, len(lst)-1
        while L <= R:
            if lst[L] != lst[R]:
                return  False
            L += 1
            R -= 1
        return True



    
# @lc code=end

