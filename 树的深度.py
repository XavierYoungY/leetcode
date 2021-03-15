# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __int__(self):
        self.depth=0
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        self.preorder(pRoot)
        return self.depth
        
    def preorder(self,root):
        if not root:
            return
        self.depth+=1
        self.preorder(root.left)
        self.preorder(root.right)
        
        
        
if __name__ == "__main__":
    main()