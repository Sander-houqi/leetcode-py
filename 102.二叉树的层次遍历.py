#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         print(root)
#         result = []
#         if not root:
#             return result

#         def iter_fun(node,level):
#             if len(result)==level:
#                 result.append([])
            
#             result[level].append(node.val)

#             if node.left:
#                 iter_fun(node.left,level+1)
            
#             if node.right:
#                 iter_fun(node.right,level+1)

#         iter_fun(root,0)
        
#         return result

from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        print(queue)
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            print('length:',level_length)
            
            for i in range(level_length):
                node = queue.popleft()
                print(node)
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels



# @lc code=end

