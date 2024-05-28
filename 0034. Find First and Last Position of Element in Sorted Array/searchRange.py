class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        return [nums.index(target), n-1-nums[::-1].index(target)] if target in nums else [-1, -1]