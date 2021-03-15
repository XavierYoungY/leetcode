# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return TreeNode类
#
class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if not pRoot:
            return None
        return self.travel(pRoot)
    
    def travel(self,root):
        if not root:
            return
        else:
            root.left,root.right=root.right,root.left
               
        root.left=self.travel(root.left)
        root.right=self.travel(root.right)
        return root