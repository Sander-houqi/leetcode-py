#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
"""使用二分查找，复杂度log2(N),注意两种形式的二分查找，主要是target的不同，相应的边界条件要变"""
class Solution:
    # 二分查找无target 判断
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     if len(nums)==0:
    #         return 0
    #     left = 0 
    #     right = len(nums)

    #     # 没有判断mid是否和target相等
    #     while(left < right):
    #         # 避免整型溢出
    #         # mid = left + (right-left)//2
    #         # 或者使用右移运算
    #         mid = (left +right) >> 1
    #         if nums[mid] < target:
    #             left = mid +1 
    #         else:
    #             right = mid
    #     return left
    
    # 二分查找target判断
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        left = 0 
        right = len(nums)-1

        while(left <= right):
            # 避免整型溢出 代替 （left+rigtht)//2
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
        return left
    

# @lc code=end

