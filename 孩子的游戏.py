# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1:
            return -1
        if n == 1:
            return 0
        f = [0]*n
        number = n
        for i in range(1, number):
            f[i] = (f[i - 1] + n) % m
            n -= 1

        return f[-1]

s=Solution()
print(s.LastRemaining_Solution(5, 3))
