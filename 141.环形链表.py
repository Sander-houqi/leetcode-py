#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # # 使用O(n）的空间复杂度
    # def hasCycle(self, head: ListNode) -> bool:
        
    #     if not head:
    #         return head

    #     tmp_list = []

    #     while head !=None:
    #         if head in tmp_list:
    #             return True
    #         tmp_list.append(head)
    #         head = head.next

    #     return False

    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return head
        
        slow = head
        fast = head

        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            
            # is 表示内存中的地址是否相同
            if fast is slow:
                return True
            
        return False
        
# @lc code=end

