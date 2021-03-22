#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        fuhao=''
        if s[0] in '-+':
            fuhao=s[0]
            s=s[1:]
        x=''
        for i in s:
            if i.isdigit():
                x+=i
            else:break
        x = int(fuhao + x)
        left=-(2**31)
        right=2**31-1
        if x<left:return left 
        elif x>right:return right
        else:return x


# @lc code=end
