# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        n=len(pushV)
        if not n:
            return False
        
        s=[]
        i=0
        j=0
        while i<n:
            if pushV[i]!=popV[j]:
                s.append(pushV[i])
                i+=1
                continue
            else:
                i+=1
                j+=1
                if s and s[-1]==popV[j]:
                    s.pop()
                    j+=1
        if s[::-1]==popV[j:]:
            return True
        if len(s):
            return False
        else:
            return True
if __name__ == '__main__':
    s=Solution()
    print(s.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))
                   
                
                
                
            