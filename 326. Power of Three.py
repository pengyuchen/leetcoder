class Solution(object):
    def isPowerOfThree(self, n):
        import math
        return False if n<=0 else (math.log10(n)/math.log10(3)).is_integer()
        