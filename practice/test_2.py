#coding=utf-8
import sys 
#str = input()
#print(str)
class linked_list(object):
    
    def __init__(self, val, next_one):
        self.val = val
        self.next_one = next_one

def reverse(head):
    if head.next_one is None:
        return None
    tail = head.next_one
    while tail.next_one is not None:
        cur = tail.next_one
        cur.next_one = head.next_one
        head.next_one = cur
        tail.next_one = tail.next_one.next_one
    return head

head = linked_list(-1,None)
head.next_one = linked_list(1,None)
head.next_one.next_one = linked_list(2, None)
head.next_one.next_one.next_one = linked_list(3, None)

reverse_linked_list = reverse(head)
cur = reverse_linked_list.next_one
while cur is not None:
    print(cur.val)
    cur = cur.next_one



