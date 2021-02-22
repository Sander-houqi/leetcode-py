#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    #双指针法，但是还能有优化空间，减少i 和 j 的的遍历步数
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        for j in range(len(nums)):
            # 条件判断要！= 而不是==
            if nums[j]!=val:
                nums[i] = nums[j]
                #后加1，注意和26题区分
                i = i + 1

        return i
# @lc code=end

