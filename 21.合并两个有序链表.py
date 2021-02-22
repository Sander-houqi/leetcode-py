#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """递归调用，一定要想清楚结束条件，等价关系"""
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     if l1 is None:
    #         return l2
    #     if l2 is None:
    #         return l1

    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next,l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l2.next,l1)
    #         return l2

    """迭代法"""
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoLists(self, l1, l2):
        prev_head = ListNode(-1)

        prev = prev_head

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next 
            else:
                prev.next = l2
                l2 = l2.next 
            prev = prev.next        
        # 有一个链表为空的判断
        prev.next = l1 if l1 is not None else l2
        print(prev)
        return prev_head.next

# @lc code=end

