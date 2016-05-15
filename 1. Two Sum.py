class Solution(object):
    def twoSum(self, nums, target):
        num_h = { num:i for i,num in enumerate(nums)}
        for i,num in enumerate(nums):
            if (target-num) in num_h and i != num_h[target-num]:
                return [i, num_h[target-num]]
