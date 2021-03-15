# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return
        
        p=pHead1 
        q=pHead2 
        while p!=q:
            p=p.next if p else pHead1
            q=q.next if q else pHead2
        return p
         