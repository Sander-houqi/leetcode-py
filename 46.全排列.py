#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #　回溯法，使用标记数组
        def dfs(nums,size,depth,path,used,res):
            
            if depth == size:
                # path 浅层深拷贝，path这里相当于一个栈
                res.append(path[:])

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    #添加结点
                    path.append(nums[i])
                    #深度优先搜索
                    dfs(nums,size,depth+1,path,used,res)
                    #撤销结点
                    used[i] = False
                    path.pop()


        n = len(nums)
        if n == 0 :
            return []

        used = [False for _ in range(n)]
        res = []
        dfs(nums,n,0,[],used,res)

        return res
        

# @lc code=end

