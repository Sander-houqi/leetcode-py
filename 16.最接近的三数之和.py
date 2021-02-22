#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        length= len(nums)
        result = 99999
        for i in range(length):

            p = i + 1
            q = length -1
            while(p<q):
                
                tmp_sum = nums[i]+nums[p]+nums[q]
                if abs(tmp_sum - target)< abs(result-target):
                    result = tmp_sum
                elif tmp_sum<target:
                    p +=1
                else:
                    q -=1
        
        return result
                
                
            

# @lc code=end

