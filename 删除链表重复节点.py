# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead: return None 
        dupl=set()
        
        pre=pHead
        cur=pre.next
        while cur:
            if pre.val==cur.val:
                dupl.add(cur.val)
            pre=cur
            cur=cur.next
        new_head=ListNode(-1)
        new_head.next=pHead
        p=new_head
        while p.next:
            if p.next.val in dupl:
                p.next=p.next.next
            else:
                p=p.next 
        return new_head.next
        
        