#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        if len(nums)<4:
            return result
        
        nums.sort()
        length = len(nums)
        for a in range(length-3):
            #这里必须是nums[a]==nums[a-1]
            if a> 0 and nums[a]==nums[a-1]: continue
            for b in range(a+1,length-2):
                # b>a+1 否则[0,0,0,0]不通过
                if b>a+1 and nums[b]==nums[b-1]: continue
                p = b+1
                q = length-1
                while(p<q):
                    tmp_sum = nums[a]+nums[b]+nums[p]+nums[q]
                    if tmp_sum == target:
                        result.append([nums[a],nums[b],nums[p],nums[q]])
                        while(p<q and nums[p]==nums[p+1]):
                            p+=1
                        while(p<q and nums[q]==nums[q-1]):
                            q-=1
                        p+=1
                        q-=1
                    elif tmp_sum < target:
                        p+=1
                    else:
                        q-=1

        return result

# @lc code=end

