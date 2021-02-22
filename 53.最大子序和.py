#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    # 另一种DP
    # 相比于官方DP 区别在于当前位置的最大和使用变量sum来代替，而不是直接替换原始数组

    # def maxSubArray(self, nums) -> int:
    #     sum = nums[0]
    #     max_sum = sum
    #     for i in range(1,len(nums)):
            
    #         if sum>0:
    #             sum = sum + nums[i]
    #         else:
    #             sum = nums[i]
            
    #         max_sum =max(max_sum,sum)

    #     return  max_sum

    # 分治法 （递归搞不懂哭）
    # def cross_sum(self, nums, left, right, p): 
    #         if left == right:
    #             return nums[left]

    #         left_subsum = float('-inf')
    #         curr_sum = 0
    #         for i in range(p, left - 1, -1):
    #             curr_sum += nums[i]
    #             left_subsum = max(left_subsum, curr_sum)

    #         right_subsum = float('-inf')
    #         curr_sum = 0
    #         for i in range(p + 1, right + 1):
    #             curr_sum += nums[i]
    #             right_subsum = max(right_subsum, curr_sum)

    #         return left_subsum + right_subsum   
    
    # def helper(self, nums, left, right): 
    #     if left == right:
    #         return nums[left]
        
    #     p = (left + right) // 2
            
    #     left_sum = self.helper(nums, left, p)
    #     right_sum = self.helper(nums, p + 1, right)
    #     cross_sum = self.cross_sum(nums, left, right, p)
        
    #     return max(left_sum, right_sum, cross_sum)
        
    # def maxSubArray(self, nums: 'List[int]') -> 'int':
    #     return self.helper(nums, 0, len(nums) - 1)

    # 同样分治法，较好理解。
    # def maxSubArray(self, nums: 'List[int]') -> int:
    #     n = len(nums)
    #     #递归终止条件
    #     if n == 1:
    #         return nums[0]
    #     else:
    #         #递归计算左半边最大子序和
    #         max_left = self.maxSubArray(nums[0:len(nums) // 2])
    #         #递归计算右半边最大子序和
    #         max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])
        
    #     #计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
    #     max_l = nums[len(nums) // 2 - 1]
    #     tmp = 0
    #     for i in range(len(nums) // 2 - 1, -1, -1):
    #         tmp += nums[i]
    #         max_l = max(tmp, max_l)
    #     max_r = nums[len(nums) // 2]
    #     tmp = 0
    #     for i in range(len(nums) // 2, len(nums)):
    #         tmp += nums[i]
    #         max_r = max(tmp, max_r)
    #     #返回三个中的最大值
    #     return max(max_right,max_left,max_l+max_r)



    # 贪心法
    # 没感觉和第一种有什么区别，只是简略了上述判断条件。
    # 还是遍历更新当前元素、当前位置的最大和，全局最大和。
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum

    #官方DP
    # 相当于维护了三个数组
    # 原始num数组
    # 当前位置的最大和，使用替换原始数组的形式
    # 全局位置的最大和数组
    # def maxSubArray(self, nums: 'List[int]') -> 'int':
    #     n = len(nums)
    #     max_sum = nums[0]
    #     for i in range(1, n):
    #         if nums[i - 1] > 0:
    #             nums[i] += nums[i - 1] 
    #         max_sum = max(nums[i], max_sum)

    #     return max_sum




# @lc code=end
if __name__ == "__main__":
    S = Solution()
    print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

