class Solution:
    def isPowerOfTwo(self, n):
        for i in range(32):
            if pow(2, i) == n:
                return True
            if pow(2, 1) > n:
                return False



class Solution:
    def isPowerOfTwo(self, n):
        for i in range(32):
            if pow(2, i) == n:
                return True
            if pow(2, 1) > n:
                return False