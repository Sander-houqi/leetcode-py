#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums , target):
        
        def left_bound(nums,target):
            if len(nums)==0:
                return -1
            
            l,r = 0 ,len(nums)
            while l<r:
                mid = l +(r-l)//2
                if nums[mid] == target:
                    r = mid
                elif nums[mid] <target:
                    l = mid + 1
                else:
                    r = mid
            print(l)
            # 防止越界
            if l>= len(nums) or nums[l]!=target:
                return -1
            
            return l

        def right_bound(nums,target):
            if len(nums)==0:
                return -1
            
            l,r = 0 ,len(nums)
            while l<r:
                mid = l +(r-l)//2
                if nums[mid] == target:
                    l = mid + 1
                elif nums[mid]<target:
                    l = mid + 1
                else:
                    r = mid
            print(r)
            if r<= 0 or nums[r-1]!=target:
                return -1
            
            return r-1
           
        return [left_bound(nums,target),right_bound(nums,target)]


# @lc code=end
# @lc code=end
if __name__ == "__main__":
    nums = [-1,0,3,3,3,5,9,12]
    target = -5
    s = Solution()
    print(s.searchRange(nums,target))

