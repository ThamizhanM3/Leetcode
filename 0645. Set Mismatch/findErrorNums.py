class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = n
        nums.sort()
        for i in range(n-1):
            if i+1 not in nums:
                x = i+1
            if nums[i] == nums[i+1]:
                nm = nums[i]
        return [nm, x]