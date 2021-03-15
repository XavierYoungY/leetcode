# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        def issame(roota,rootb):
            if not rootb:
                return True
            if not roota:
                return False
            if roota.val!=rootb.val:
                return False
            return issame(roota.left,rootb.left) and issame(roota.right,rootb.right)
        
        return issame(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
        