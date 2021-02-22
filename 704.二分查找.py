#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    # def search(self, nums, target) -> int:
        
    #     if len(nums)==0:
    #         return 0

    #     left ,right = 0 ,len(nums)-1
        
    #     #边界条件必须小于等于，否则nums长度为1时不满足
    #     while(left<=right):
    #         # 避免整型溢出
    #         mid = left +(right-left)//2
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid]< target:
    #             left = mid+1
    #         else:
    #             right = mid-1

    #     return -1

    # 博客https://www.cnblogs.com/kyoner/p/11080078.html 讲得很好
    def search(self, nums, target) -> int:

        if len(nums)==0: return 0

        # len(nums) 不需要-1
        l,r = 0,len(nums)

        #如果没有=,right的条件不是mid-1
        while(l<r):
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid

        return -1


# @lc code=end
if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 0
    s = Solution()
    print(s.search(nums,target))

