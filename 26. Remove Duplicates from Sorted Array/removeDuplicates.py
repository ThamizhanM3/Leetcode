class Solution:
    def removeDuplicates(self, nums):
        i = 0
        c = 0
        n = len(nums)
        while i < len(nums)-1:
            if not n-1:
                break
            if nums[i] == nums[i+1]:
                nums.append(nums.pop(i+1))
                c += 1
            else:
                i += 1
            n -= 1
        return len(nums) - c