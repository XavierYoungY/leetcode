# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def __init__(self):
        self.depth=0
        self.out={}
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return [[]]
        queue=[]
        while queue:
            tmp=queue.pop 
            
            if self.depth not in self.out:
                self.out[self.depth]=[tmp.val]
            else:
                self.out[self.depth].append(tmp.val)
                
            if tmp.left:
                queue.append(tmp.left)
                self.depth+=1
            if tmp.right:
                queue.append(tmp.right)
                self.depth+=1
                
                
if __name__ == "__main__":
    s=Solution()
    