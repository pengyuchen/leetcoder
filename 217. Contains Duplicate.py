class Solution(object):
    def containsDuplicate(self, nums):
        from collections import defaultdict
        l = defaultdict(lambda:0)
        for num in nums:
            l[num] += 1
            if l[num] == 2:
                return True
        return False
