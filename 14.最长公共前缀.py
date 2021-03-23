#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==0: return ''
        if len(strs)==1: return strs[0]

        def prefix(a,b):
            out=''
            minl=min(len(a),len(b))
            for i in range(minl):
                if a[i]==b[i]:
                    out+=a[i]
                else: break
            return out       
        maxprefix =strs[0]
        for i in range(1,len(strs)):
            a = strs[i]
            maxprefix=prefix(a,maxprefix)
        return maxprefix


s= Solution()
s.longestCommonPrefix(["cir", "car"])

# @lc code=end
