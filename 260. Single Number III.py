class Solution(object):
    def singleNumber(self, nums):
        from operator import xor
        two_num_xor = reduce(xor, nums)
        two_num_filter = two_num_xor & -two_num_xor
        ans = [0, 0]
        for num in nums:
            if num & two_num_filter != 0:
                ans[0] ^= num
            else:
                ans[1] ^= num

        return ans
