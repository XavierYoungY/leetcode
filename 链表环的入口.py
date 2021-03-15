# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next: return None
        fast=pHead
        slow=pHead
        while slow and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break
        
        fast=pHead
        while(fast!=slow):
            fast=fast.next
            slow=slow.next 
            
        return fast
            
            