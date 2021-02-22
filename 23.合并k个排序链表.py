#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if len(lists)==0:
            return -1

        def merge2lists(l1,l2):

            prev_head = ListNode(-1)

            prev = prev_head

            while l1 and l2:

                if l1.val <=l2.val:
                    prev.next = l1
                    l1 = l1.next

                else:
                    prev.next =l2
                    l2 = l2.next

                prev = prev.next

            prev.next = l1 if l1 is not None else l2

            return prev_head.next

        def merge(lists,low,high):

            if low == high:
                return lists[low]

            mid = low + (high - low) //2

            l1 = merge(lists,low,mid)
            l2 = merge(lists,mid+1,high)

            return merge2lists(l1,l2)


        return merge(lists,0,len(lists)-1)
        
# @lc code=end

