#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # 二进制直接相加
        carry = 0 
        result = ''

        length= max(len(a),len(b))
        a,b = a.zfill(length),b.zfill(length)

        for i ,j in zip(a[::-1],b[::-1]):
            carry = carry + int(i)+int(j)
            # 连接顺序要注意，否则需要反转
            result = str(carry%2)+ result
            carry //= 2
        
        if carry:
            result = '1'+result
        return result
        
# @lc code=end

