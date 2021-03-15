# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers) / 2
        numbers.sort()
        i = numbers[len(numbers) // 2]
        if numbers.count(i) > length:
            return i
        return 0


if __name__ == "__main__":
    a = Solution()
    print(a.MoreThanHalfNum_Solution([1,1,2]))
