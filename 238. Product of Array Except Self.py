class Solution(object):
    def productExceptSelf(self, nums):
        from operator import mul

        left, right = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]

        nums.reverse()
        for i in range(1, len(nums)):
            right[i] = nums[i-1] * right[i-1]
        right.reverse()

        return map(lambda x: mul(*x),zip(left, right))
