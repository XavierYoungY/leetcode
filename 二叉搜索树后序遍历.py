# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        
        def varify(i,j):
            if i>=j:
                return True
            index=i 
            while sequence[index]<sequence[j]: index+=1
            left=index-1
            while sequence[index]>sequence[j]:index+=1
            right=index
            
            return index==j and varify(i,left) and varify(left,right-1)
        return varify(0,len(sequence)-1)