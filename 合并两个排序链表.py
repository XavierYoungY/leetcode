# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head=pointer=ListNode(0)
        p=pHead1
        q=pHead2
        
        while p and q:
            if p.val<=q.val:
                pointer.next=p 
                p=p.next
                pointer=pointer.next
            else:
                pointer.next=q
                q=q.next
                pointer=pointer.next
                
        if p:
            pointer.next=p 
        if q:
            pointer.next=q
            
        return head.next