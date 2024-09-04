class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        return max(nums) if len(nums) < 3 else sorted(nums)[-3]