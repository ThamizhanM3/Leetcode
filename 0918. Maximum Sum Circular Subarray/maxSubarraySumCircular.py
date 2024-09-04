class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        m1 = max(nums)
        s = 0
        for i in nums:
            s += i
            if s < m1:
                m1 = s
            if s > 0:
                s = 0
        m2 = min(nums)
        s = 0
        for i in nums:
            s += i
            if s > m2:
                m2 = s
            if s < 0:
                s = 0
        return max(m2, sum(nums)-m1) if max(m2, sum(nums)-m1) > 0 else m2