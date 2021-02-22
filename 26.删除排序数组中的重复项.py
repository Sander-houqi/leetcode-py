#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
        
    #     # 正向遍历数组，数组删除会导致数组长度变化，所以要反向删除
    #     #另外注意range(10,0,-1) 是左闭右开[10,0)
    #     for i in range(len(nums)-1,0,-1):
    #         print(nums[i],nums[i-1])
    #         if nums[i]==nums[i-1]:
    #             nums.pop(i)
    #     return len(nums)


    def removeDuplicates(self, nums: List[int]) -> int:
        
        #双指针遍历
        # if len(nums)==0:
        #     return 0
        
        i = 0 
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i = i +1
                nums[i] = nums[j]
        
        #因为最后要返回数组长度，所以i+1
        return i+1
        # 加上and 
        # 如果要删除多余的元素，可以加上，但题目中说不考虑数组长度
        # del nums[i+1:]
        # return len(nums) and i + 1

        

    

# @lc code=end

