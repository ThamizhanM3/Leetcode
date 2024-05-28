class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 1
        j = 0
        while i < len(nums):
            if nums[i] == val:
                i += 1
                continue
            if nums[j] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            else:
                j += 1
            if j == i:
                i += 1
        return len(nums) - nums.count(val)