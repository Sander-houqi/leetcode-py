#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
"""构建栈的方式解决"""
class Solution:
    def isValid(self, s: str) -> bool:

        map = {"}":"{",")":"(","]":"["}

        stack=[]

        for char in s:

            if char in map:
                
                stack_ele = stack.pop() if stack else "!"

                if map.get(char) !=stack_ele:
                    return False
            else:
                stack.append(char)

        # stack 不为空则不合法
        return not stack
        
# @lc code=end

