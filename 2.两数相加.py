#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1x,l2x=[],[]
        while l1:
            l1x.append(l1.val)
            l2x.append(l2.val)
            l1=l1.next
            l2=l2.next
        l1 = int(''.join(l1x))
        l2 = int(''.join(l2x))
        out=str(l1+l2)
        head=ListNode() 
        p=head    
        for i in out:
            p.val

# @lc code=end
