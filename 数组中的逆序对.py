# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count=0
    def InversePairs(self, data):
        n=len(data)
        if n<=0: return data
        self.mergesort(data)
        return self.count % 1000000007
        
    def mergesort(self,data):
        n=len(data)
        if n<=1:
            return data
        
        left_list=self.mergesort(data[:n//2])
        right_list=self.mergesort(data[n//2:])
        l_p=0
        r_p=0
        out=[]
        
        while(l_p<len(left_list) and r_p<len(right_list)):
            if left_list[l_p]<right_list[r_p]:
                out.append(left_list[l_p])
                l_p+=1
            else:
                out.append(right_list[r_p])
                r_p+=1
                self.count+=len(left_list)-l_p
        out+=left_list[l_p:]
        out+=right_list[r_p:]
        return out
                
        