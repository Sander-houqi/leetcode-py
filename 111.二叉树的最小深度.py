#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 注意一共有四个出口
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right)+1
        if root.right is None:
            return self.minDepth(root.left) +1
        
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
# @lc code=end

