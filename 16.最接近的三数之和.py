#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if n<=2: return
        nums.sort()
        out=None
        for first in range(n-2):
            if first>1 and nums[first]==nums[first-1]: continue

            for second in range(first+1,n-1):
                if second>first+1 and nums[second]==nums[second-1]: continue
                for third in range(second+1,n):
                    if third>second+1 and nums[third]==nums[third-1]: continue
                    if out is None:
                        out=nums[first]+nums[second]+nums[third]
                        gap=abs(out-target)
                    else:
                        newgap = abs(nums[first] + nums[second] + nums[third]-target)
                        if newgap<gap:
                            gap=newgap
                            out = nums[first] + nums[second] + nums[third]

        return out

# @lc code=end
