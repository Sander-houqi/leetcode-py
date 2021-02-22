#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:

    # # 时间复杂度O(m+n) 空间复杂度O(m)
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     # 必须是[:m],否则m后的元素可能未排序列
    #     num1_cp = nums1[:m]
    #     # 不改变nums1的地址，只改变其值
    #     nums1[:]=[]

    #     # 定义两个指针
    #     p1 = 0
    #     p2 = 0 

    #     # 只能用while
    #     while p1<m and p2<n:
    #         if num1_cp[p1]<=nums2[p2]:
    #             nums1.append(num1_cp[p1])
    #             p1 += 1
    #         else:
    #             nums1.append(nums2[p2])
    #             p2 += 1 
        
    #     # 追加剩余，注意边界
    #     if p1<m:
    #         nums1[p1+p2:]=num1_cp[p1:]

    #     if p2<n:
    #         nums1[p1+p2:]=nums2[p2:]

    # 时间复杂度O(m+n) 空间复杂度O(1),从后向前，使用O(1)空间
    def merge(self, nums1 ,m, nums2 ,n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 从后向前
        p1 = m-1
        p2 = n-1

        # 追踪插入位置
        p = m+n-1

        
        while p1>=0 and p2>=0:

            if nums1[p1]<nums2[p2]:
                nums1[p]= nums2[p2]
                p2 -=1

            else:
                nums1[p]= nums1[p1]
                p1 -=1
            
            p -=1
            print(p1,p2)
        
        # 如果m<n,nums2中且还存在比nums中最小的元素小的情况
        # 或者nums1未为空
        nums1[:p2+1] = nums2[:p2+1]



if __name__ == "__main__":
    s = Solution()

    nums1=[5,14,15,20]
    # nums2=[2,4,5]
    nums2=[0,2,4,5,6,8,9,10]
    nums1 = nums1+[0]*len(nums2)
    s.merge(nums1,4,nums2,len(nums2))
    print(nums1)
        

        

# @lc code=end

