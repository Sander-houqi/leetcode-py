#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 归并排序
        def merge_sort(arr_list):
            if len(arr_list)==1:
                return arr_list
            
            mid = len(arr_list)//2
            left = merge_sort(arr_list[:mid])
            right = merge_sort(arr_list[mid:])

            return merge(left,right)

        def merge(left,right):
            res =[]
            while len(left)>0 and len(right)>0:
                if left[0]<=right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
            
            res += left
            res += right

            return res

        return merge_sort(nums)

    # # 快速排序
    # def sortArray(self, nums: List[int]) -> List[int]:


    #     def partition(nums,low,high): 
    #         i = low -1
    #         # 主元，最后一个
    #         pivot =  nums[high]

    #         for j in range(low,high):
    #             if nums[j]<= pivot:
    #                 i +=1
    #                 # 如果小于主元，以此交换到左侧
    #                 nums[i] , nums[j] = nums[j], nums[i]

    #         nums[i+1],nums[high]= nums[high],nums[i+1]

    #         return i+1

    #     def quick_sort(nums,low,high):
    #         if low < high:
    #             pivot = partition(nums,low,high)
    #             quick_sort(nums,low,pivot-1)
    #             quick_sort(nums,pivot+1,high)

        
    #     quick_sort(nums,0,len(nums)-1)

    #     return nums




                



# @lc code=end


