#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        # 类全局变量
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)

            # 最大贡献值
            tmp_sum = node.val + left + right

            # 最大路径和
            self.max_sum = max(self.max_sum,tmp_sum)

            return node.val + max(left,right)

        dfs(root)
        return self.max_sum



# @lc code=end

