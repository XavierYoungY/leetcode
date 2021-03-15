# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin or (len(pre)!=len(tin)):
            return None
        root=TreeNode(pre[0])
        pos=tin.index(pre[0])
        
        pre_left=pre[1:pos+1]
        pre_right=pre[pos+1:]
        tin_left=tin[:pos]
        tin_right=tin[pos+1:]
        
        left_tree=self.reConstructBinaryTree(pre_left,tin_left)
        right_tree=self.reConstructBinaryTree(pre_right,tin_right)
        root.left=left_tree
        root.right=right_tree
        return root
        
        