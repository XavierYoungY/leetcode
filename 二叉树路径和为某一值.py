# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        all_list=[]
        single_list=[]
        
        def preorder(node,total):
            if not node: return
            single_list.append(node.val)
            total-=node.val
            if total==0 and not node.left and not node.right:
                all_list.append(single_list[:])
            preorder(node.left,total)
            preorder(node.right,total)
            single_list.pop()
            
        preorder(root,expectNumber)
        return all_list
            
            

            
        