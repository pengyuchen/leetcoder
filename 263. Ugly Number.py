class Solution(object):
    def isUgly(self, num):
        if num == 0:
            return False
        else:
            for ugly in [2,3,5]:
                while (num%ugly==0):
                    num/=ugly
            return num == 1
