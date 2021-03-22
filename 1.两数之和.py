#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index,num in enumerate(nums):
            hashmap[num]=index
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j and i!=j:
                return [i,j]



# @lc code=end
