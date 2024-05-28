class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        l = 0
        h = len(nums)-1
        while True:
            m = (l+h)//2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            if nums[m+1] > nums[m-1]:
                l = m+1
            else:
                h = m-1



class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, -inf)
        nums.append(-inf)
        l = 0
        h = len(nums)-1
        while True:
            m = (l+h)//2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m-1
            if nums[m+1] > nums[m-1]:
                l = m+1
            else:
                h = m-1



class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        for i in range(1, n-1):
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                return i
        if nums[-1] > nums[-2]:
            return n-1
