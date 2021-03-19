# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        def xx(l,s):
            n=(s+0.5*l**2+0.5*l)/(l+1)
            if n<s and n==int(n) and n-l>0:
                return int(n)
            return 0
            
        mid=tsum//2+1
        l,n=1,1
        out=[]
        for l in range(mid):
            n=xx(l,tsum)
            if n:
                out.append([l,n])
            
                
        if not len(out):
            return []
        res=[]
        for i in out:
            l=i[0]
            n=i[1]
            res.append(list(range(n-l,n+1)))
            
        return sorted(res, key=lambda i:i[0])
    
    
s=Solution()
a=s.FindContinuousSequence(100)
print(a)
    
    
    
    
              