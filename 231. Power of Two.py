class Solution(object):
    def isPowerOfTwo(self, n):
        from math import log10
        return False if n <= 0 else (log10(n)/log10(2)).is_integer()
        