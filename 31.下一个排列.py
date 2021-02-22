#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums)<=1:
            return
        
        length = len(nums)
        i = length-2
        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1

        if (i>=0):
            j = length-1
            while(j>=0 and nums[i]>=nums[j]):
                j-=1

            # swap
            nums[i],nums[j]=nums[j],nums[i]

        # reverse
        k = length -1
        i = i+1
        while(i<k):
            nums[i],nums[k]= nums[k],nums[i]
            i+=1
            k-=1
        
    
if __name__ == "__main__":
    a = Solution()
    m = [3,2,1,0]
    a.nextPermutation(m)
    print(m)


# @lc code=end

