#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    # O(n^2) 超时
    # def maxArea(self, height: List[int]) -> int:

    #     if len(height)<2:
    #         return 0

    #     p = 0 
    #     n = len(height)-1
    #     max_area = 0
    #     while(p<=n):
    #         q = p + 1
    #         while(q<=n):
                
    #             h = min(height[p],height[q])
    #             w = q - p
    #             tmp_array = h * w
    #             if tmp_array>max_area:
    #                 max_area = tmp_array

    #             q = q + 1

    #         p = p + 1 
        
    #     return max_area

    def maxArea(self, height: List[int]) -> int:

        if len(height)<2:
            return 0

        p = 0 
        q = len(height)-1
        max_area = 0

        while(p<q):

            h = min(height[p],height[q])
            w = q - p
            tmp_array = h * w
            if tmp_array>max_area:
                max_area = tmp_array

            if height[p]<height[q]:
                p += 1
            else:
                q -= 1
            
        return max_area

       
# @lc code=end

