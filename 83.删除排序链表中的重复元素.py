#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        p = head
        q = head.next
        while p and q:
            if p.val == q.val:
                q = q.next
                p.next = q
                print(p.val)
            else:
                p = p.next
                q= q.next

        return head

# @lc code=end

