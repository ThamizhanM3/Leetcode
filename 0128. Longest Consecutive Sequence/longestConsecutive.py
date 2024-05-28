class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0
        c = 1
        m = 1
        for i in range(n-1):
            if nums[i]+1 == nums[i+1]:
                c += 1
            else:
                c = 1
            if m < c:
                m = c
        return m