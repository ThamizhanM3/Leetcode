class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = [max(nums), nums.index(max(nums))]
        nums.pop(m[1])
        for i in nums:
            if i*2 > m[0]:
                return -1
        return m[1]