#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
    #     #虚拟节点
    #     root = ListNode(0)
    #     root.next= head

    #     p = q = root

    #     # 间隔为n，差值为n+1
    #     while n+1:
    #         q = q.next
    #         n-=1
    #     while q:
    #         q = q.next
    #         p = p.next

    #     p.next = p.next.next

    #     return root.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next


# @lc code=end

