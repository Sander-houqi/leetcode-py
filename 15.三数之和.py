#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    # 排序+双指针
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res =[]
        length = len(nums)
        if(not nums or length<3):
            return []

        nums.sort()
        for i in range(length):
            
            if nums[i]>0:
                return res
            if(i>0 and nums[i]==nums[i-1]):
                continue

            p,k = i+1,length-1
            while(p<k):
                if (nums[i] + nums[p] + nums[k]==0):
                    res.append([nums[i],nums[p],nums[k]])
                    # 跳过重复解
                    while(p<k and nums[p]==nums[p+1]):
                        p += 1
                    while(p<k and nums[k]==nums[k-1]):
                        k -= 1
                    p+=1
                    k-=1
                elif (nums[i] + nums[p] + nums[k])>0:
                    k-=1
                else:
                    p+=1
        
        return res

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
        
    #     n=len(nums)
    #     res=[]
    #     if(not nums or n<3):
    #         return []
    #     nums.sort()
    #     res=[]
    #     for i in range(n):
    #         if(nums[i]>0):
    #             return res
    #         if(i>0 and nums[i]==nums[i-1]):
    #             continue
    #         L=i+1
    #         R=n-1
    #         while(L<R):
    #             if(nums[i]+nums[L]+nums[R]==0):
    #                 res.append([nums[i],nums[L],nums[R]])
    #                 while(L<R and nums[L]==nums[L+1]):
    #                     L=L+1
    #                 while(L<R and nums[R]==nums[R-1]):
    #                     R=R-1
    #                 L=L+1
    #                 R=R-1
    #             elif(nums[i]+nums[L]+nums[R]>0):
    #                 R=R-1
    #             else:
    #                 L=L+1
    #     return res

                    
                    



# @lc code=end

