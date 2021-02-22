#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    # def romanToInt(self, s: str) -> int:
        
    #     roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
    #             "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}

    #     num =0
    #     for i,char in enumerate(s):
    #         if i>0 and s[i-1]+char in roman:
    #             continue

    #         if char != "I" and char!="X" and char!="C":
    #             num += roman.get(char)
    #         else:
    #             if i<len(s)-1 and char+s[i+1] in roman:
    #                 num += roman.get(char+s[i+1])
    #             else:
    #                 num += roman.get(char)
        
    #     return num

    """
    一个比较有趣的解法：

    构建一个字典记录所有罗马数字子串，注意长度为2的子串记录的值是（实际值 - 子串内左边罗马数字代表的数值）
    这样一来，遍历整个 ss 的时候判断当前位置和前一个位置的两个字符组成的字符串是否在字典内，如果在就记录值，不在就说明当前位置不存在小数字在前面的情况，直接记录当前位置字符对应值
    举个例子，遍历经过 IVIV 的时候先记录 II 的对应值 11 再往前移动一步记录 IVIV 的值 33，加起来正好是 IVIV 的真实值 44。
    max 函数在这里是为了防止遍历第一个字符的时候出现 [-1:0][−1:0] 的情况
    """
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))



# @lc code=end

