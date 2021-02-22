#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 分析题目应该是让实现进位
        
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]=digits[i]+1
                return digits
        # 高位补1
        digits.insert(0,1)

        return digits
# @lc code=end

