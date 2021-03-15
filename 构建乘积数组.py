# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        n=len(A)
        left = [1] * n
        right = [1] * n
        for i in range(0,len(A)):
            if i+1<=n-1:
                left[i+1]*=left[i]*A[i]
            j=n-i
            if j-1>=0 and j<=n-1:
                right[j-1]=A[j]*right[j]
        B=[]
        for i in range(n):
            B.append(left[i]*right[i])

        return B

if __name__ == "__main__":
    a = Solution()
    print(a.multiply([1,2,3,4,5]))