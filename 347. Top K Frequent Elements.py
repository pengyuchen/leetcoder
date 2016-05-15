class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import Counter
        return map(lambda x : x[0], Counter(nums).most_common(k))
