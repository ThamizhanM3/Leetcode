class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = [False for i in range(n)]
        opt = []
        for i in nums:
            if a[i-1]:
                opt.append(i)
            else:
                a[i-1] = True
        return opt



class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = []
        opt = []
        for i in range(n):
            c.append(0)
        for i in nums:
            c[i-1] += 1
        for i in range(n):
            if c[i] == 2:
                opt.append(i+1)
        return opt