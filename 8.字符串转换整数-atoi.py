# #
# # @lc app=leetcode.cn id=8 lang=python3
# #
# # [8] 字符串转换整数 (atoi)
# #

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        
        INT_MIN = -2**31
        INT_MAX = 2**31 -1

        valid_char = ['+','-','0','1','2','3','4','5','6','7','8','9']
        text = str.strip(' ')
        if len(text)==0 or (text[0] not in valid_char):
            return 0

        sign = 1
        if text[0]=='-':
            sign = -1
            text=text[1:]
        elif text[0]=='+':
            sign = 1
            text=text[1:]

        result = 0
        for i in text:
            if i in valid_char[2:]:
                result = result*10+int(i)
            else:
                break
        result = sign*result
        if result<INT_MIN:
            return INT_MIN
        elif result>INT_MAX:
            return INT_MAX
        
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("words and 987"))

# # @lc code=end


