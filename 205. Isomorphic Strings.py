class Solution(object):
    def isIsomorphic(self, s, t):
        from itertools import groupby
        def helper(s,t): 
            return sum(1 for _,l in groupby(sorted(zip(s,t)),key=lambda x:x[0]) if len(set(l)) != 1)
        return helper(s,t)+helper(t,s) == 0
        