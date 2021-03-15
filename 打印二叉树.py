# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        stack=[root]
        nodes=[]
        while stack:
            a=stack.pop(0)
            nodes.append(a.val)
            if a.left:
                stack.append(a.left)
            if a.right:
                stack.append(a.right)
                
        return nodes