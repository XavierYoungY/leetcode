# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):

        for i in range(len(array)):
            if target in array[i]:
                return 'true'
        return 'false'


while True:
    try:
        S = Solution()
        L = list(eval(raw_input()))
        array = L[1]
        target = L[0]
        print(S.Find(target, array))
    except:
         break