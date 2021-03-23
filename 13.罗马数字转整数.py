#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        keys= sorted(list(table.keys()),reverse=True)
        num=0
        while s:
            for k in keys:
                tmp=table[k]
                if s[0]==tmp:
                    num+=k
                    s=s[1:]
                    break
                if s[:2] == tmp:
                    num += k
                    s = s[2:]
                    break
        return num

# s=Solution()
# s.romanToInt('III')

# @lc code=end
