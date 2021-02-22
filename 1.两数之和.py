#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

"""构建hashmap,即数和索引的映射，遍历的同时查字典，时间复杂度O(n),空间复杂度O(n)"""
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,num in enumerate(nums):
            #dict[i]会产生越界，用dict.get()
            if map.get(target-num) is not None:
                return [i,map.get(target-num)]
            map[num]=i #放在if之后，解决列表重复问题

# @lc code=end

