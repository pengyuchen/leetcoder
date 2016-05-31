class Solution(object):
    def intersect(self, nums1, nums2):
        from collections import Counter
        ans = []
        nums2_hash = Counter(nums2)
        for num in nums1:
            if nums2_hash[num] != 0:
                ans.append(num)
                nums2_hash[num] -= 1
        return ans
