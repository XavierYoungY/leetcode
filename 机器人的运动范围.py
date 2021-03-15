# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        num=0
        for i in range(rows):
            for j in range(cols):
                if (self.sumi(i)+self.sumi(j))<=threshold:
                    num+=1
                elif (rows<=1 or cols<=1):
                    return num
               
        return num
                      
    def sumi(self,x):
        count=0
        while(x):
            count+=x%10
            x=x/10
        return count
    
if __name__ == "__main__":
    s=Solution()
    print(s.movingCount(5,10,10))