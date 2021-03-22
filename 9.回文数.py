#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        if x==0: return True
        x1=str(x)
        s=str(x).rstrip('0')
        if x1!=s: return False
        if s==s[::-1]: return True
        else: return False

# @lc code=end

