#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #　第一次相遇时，快指针指向head,那么再次相遇时就是入环点
    def detectCycle(self, head: ListNode) -> ListNode:

        slow = fast = head

        while True:
            if not (fast and fast.next): return None

            fast = fast.next.next
            slow = slow.next
            #　第一次相遇
            if fast == slow:
                break
        
        # fast指向头结点，slow保持不变
        fast = head
        while fast!=slow:
            fast,slow = fast.next,slow.next

        return fast
        
# @lc code=end

