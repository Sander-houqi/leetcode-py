#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre	

# @lc code=end

if __name__ == "__main__":
    s =Solution()
    n1 = ListNode(100)
    n1.next = ListNode(200)
    n1.next.next = ListNode(300)
    n1.next.next.next = ListNode(400)
    print(s.reverseList(n1))
