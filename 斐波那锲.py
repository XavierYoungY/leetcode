# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n <= 1: return n
        else:
            a = 0
            b = 1
            for i in range(2, n + 1):
                c = a + b
                a = b
                b = c
        return c

if __name__ == "__main__":
    f=Solution()
    for i in range(1,10):
        print(f.Fibonacci(i))