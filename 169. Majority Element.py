class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]
