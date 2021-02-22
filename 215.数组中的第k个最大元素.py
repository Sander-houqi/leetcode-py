#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

import random

# @lc code=start
class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     #太取巧了
    #     sort_num = sorted(nums)
    #     return sort_num[len(nums)-k]


    # 快速排序(超时。。。)
    # def findKthLargest(self, nums: List[int], k: int) -> int:

        
    #     def partition(nums,low,high):
            
    #         i = low -1
    #         pivot = nums[high]
    #         for j in range(low,high):
    #             if nums[j]<= pivot:
    #                 i += 1
    #                 nums[i] ,nums[j] = nums[j], nums[i]
            
    #         nums[i+1],nums[high] = nums[high],nums[i+1]
            
    #         return i+1

    #     def quicksort(nums,low,high):
    #         if low<high:
    #             pivot =  partition(nums,low,high)
    #             quicksort(nums,low ,pivot-1)
    #             quicksort(nums,pivot+1,high)

    #     quicksort(nums,0,len(nums)-1)
    #     return nums[len(nums)-k]



     # 快速选择  
     # 时间复杂度O(n),n+1/2n+1/4n+...,以n为底，1/2为比的等比数列求和
    def findKthLargest(self, nums: List[int], k: int) -> int:

        
        def partition(nums,low,high):
            
            i = low -1
            pivot = nums[high]
            for j in range(low,high):
                if nums[j]<= pivot:
                    i += 1
                    nums[i] ,nums[j] = nums[j], nums[i]
            
            nums[i+1],nums[high] = nums[high],nums[i+1]
            
            return i+1

        # # random init
        # def partition(nums,low,high):
            
        #     i = low -1
        #     random_index = random.randint(low,high)
        #     nums[high],nums[random_index] = nums[random_index],nums[high]
            
        #     pivot = nums[high]
        #     for j in range(low,high):
        #         if nums[j]<= pivot:
        #             i += 1
        #             nums[i] ,nums[j] = nums[j], nums[i]
            
        #     nums[i+1],nums[high] = nums[high],nums[i+1]
            
        #     return i+1


        n = len(nums)
        target = n - k
        left = 0
        right = n -1

        while(left<=right):
            index = partition(nums,left,right)
            if index ==target:
                return nums[index]
            elif index<= target:
                left = index + 1
            else:
                right = index -1
        


    



# @lc code=end

