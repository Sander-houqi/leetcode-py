#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        root = ListNode(0)
        root.next = head
        prev= root
        l = r = head
        # 第二个指针移动到指定位置
        interval = n - m+1
        num = n -m +1
        while interval:
            r = r.next
            interval-= 1
        # 双指针移动
        while m-1:
            prev = prev.next
            l = l.next
            r = r.next
            m -= 1
        # 反转局部链表
        
        st,end = prev,l
        st.next = None
        while num:
            tmp = l.next
            l.next = prev
            prev = l
            l = tmp
            num-= 1

        st.next = prev
        end.next = r

        return root.next


def print_linked_list(listNode):
    list = []
    while listNode:
        list.append(listNode.val)
        listNode = listNode.next
    return list


if __name__ == "__main__":
    s =Solution()
    n1 = ListNode(1)
    n1.next = ListNode(2)
    n1.next.next = ListNode(3)
    n1.next.next.next = ListNode(4)
    n1.next.next.next.next = ListNode(5)
    result = s.reverseBetween(n1,2,4)
    print(print_linked_list(result))


# @lc code=end

