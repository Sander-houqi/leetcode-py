#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
    #     from queue import Queue
    #     if not root:
    #         return []
    #     q = Queue()
    #     q.put(root)
    #     result =[]
        
    #     while(q.qsize()):
    #         size = q.qsize()
    #         tmp =[]
            
    #         for _ in range(size):
    #             r = q.get()
    #             tmp.append(r.val)

    #             if r.left:
    #                 q.put(r.left)
                
    #             if r.right:
    #                 q.put(r.right)

            
    #         result.append(tmp)
        
    #     return result

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        queue = [root]
        result = []
        while queue:

            size = len(queue)
            tmp = []

            for _ in range(size):
                # 父节点出队列，子节点入队
                r = queue.pop(0)
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)

            result.append(tmp)

        return result


# @lc code=end

