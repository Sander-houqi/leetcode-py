#coding=utf-8
import sys 

class MList:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def revers(l):
    start = l
    temp = l
    while temp:
        if not temp.next:
            end = temp
        temp = temp.next
    curr = end
    while start.value!=end.value:
        print(start.value)
        temp = start.next
        start.next = curr.next
        print('curr:',curr.value)
        curr.next = start
        start = temp
    return end
if __name__ == '__main__':
    l3 = MList(3)
    l2 = MList(2,l3)
    l1 = MList(1,l2)
    l0 = MList(0,l1)
    rever_list = revers(l0)
    while rever_list:
        print('a:',rever_list.value)
        rever_list = rever_list.next