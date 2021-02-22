#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 一种思路是先做转置，然后在反转每一行。
        # 复杂度（O(N_2)）
        N = len(matrix)
        for i in range(N):
            for j in range(i,N):
                tmp = matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i] =tmp
        
        for i in range(N):
            for j in range(N//2):
                tmp = matrix[i][j]
                matrix[i][j]= matrix[i][N-1-j]
                matrix[i][N-1-j]=tmp

        # 另一种找规律，内部矩形旋转。有时间在写

# @lc code=end

