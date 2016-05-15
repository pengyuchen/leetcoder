class Solution(object):
    def countBits(self, num):
        import math
        result = [0]
        for i in range(int(math.ceil(math.log(num+1,2)))):
            result.extend([n+1 for n in result])
        return result[0:num+1]