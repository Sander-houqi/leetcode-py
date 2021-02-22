#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    # 二分查找
    # def mySqrt(self, x: int) -> int:
        
    #     l,r,result = 0 ,x ,0
    #     while l<=r:
    #         mid = (l+r)//2
    #         print(l,r,mid)
    #         if mid**2 <= x:
    #             result = mid
    #             print('res:',result)
    #             l = mid +1
    #         else:
    #             r = mid -1
    #     print(result)
    #     return result

    def mySqrt(self, x: int) -> int:
        
        l,r = 0 , x
        while(l<=r):
            mid = (l+r)//2
            res = mid**2
            if res == x:
                return mid
            elif res< x :
                l = mid +1
            else:
                r = mid -1
        print(l,r)
        return r

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.mySqrt(8)