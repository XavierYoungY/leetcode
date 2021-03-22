#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p: return True

        if s and not p: return False

        if not s and p:
            if p[0:2]=='.*':
                return isMatch(s,p[2:])
            else: return False
        if s and p:
            if s[0]==p[0] or p[0]=='.':
                

# @lc code=end

