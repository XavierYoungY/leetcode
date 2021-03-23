#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        n=len(nums)
        if n<=2: return []
        nums.sort()
        out=[]
        for first in range(n-2):
            if first>0 and nums[first]==nums[first-1]: continue
            third=n-1
            for second in range(first+1,n-1):
                if second>first+1 and nums[second]==nums[second-1]: continue
                while third>second and nums[first]+nums[second]+nums[third]>0:
                    third-=1
                if second==third: break
                if nums[first]+nums[second]+nums[third]==0:
                    out.append(sorted([nums[first],nums[second],nums[third]]))



        
        return out

# s=Solution()
# s.threeSum([-1, 0, 1, 2, -1, -4])
# @lc code=end
