# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s=[]
        self.dict={}
    def FirstAppearingOnce(self):
        # write code here
        for char in self.s:
            if self.dict[char]==1:
                return char
        return '#'
    def Insert(self, char):
        # write code here
        self.s.append(char)
        if char in self.dict:
            self.dict[char]+=1
        else:
            self.dict[char]=1
            
            
            
if __name__ == '__main__':
    s=Solution()
    s.Insert("google")
    s.FirstAppearingOnce()
    