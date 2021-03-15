# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or pHead.next==None:
            return pHead
        p=pHead
        q=None
        while p:          
            tmp=p 
            p=p.next
            tmp.next=q
            q=tmp
            
                
        return q
            
            