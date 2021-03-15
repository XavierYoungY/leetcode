# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code her
        array=array[::-1]
        for i in array:
            if i>tsum:
                continue
            if (tsum-i) in array:
                return [tsum-i,i] 
        return []

if __name__ == "__main__":
    f = Solution()
    f.FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15)
