#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        # dp=[[0]*(n-1) for i in range(n-1)]

        i,j=0,n-1
        maxv = min(height[i], height[j]) * (j - i)

        while i < j:
            if height[i]<height[j]:
                i+=1
                if i==j: break
            else:
                j-=1
                if i == j: break
            maxv = max(maxv, min(height[i], height[j]) * (j - i))

        return maxv
# @lc code=end
