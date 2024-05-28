class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            j = 0
            i = 1
            while i < len(nums):
                if nums[i] == 0:
                    i += 1
                elif nums[j] == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                    i += 1
                else:
                    j += 1
                if j == i:
                    i += 1