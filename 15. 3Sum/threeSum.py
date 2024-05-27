class Solution:
    def threeSum(self, nums):
        op = set()
        nums.sort()
        for z in range(len(nums)):
            x = nums[z+1:]
            i = z+1
            j = len(nums)-1
            t = nums[z]*(-1)
            while i<j:
                if nums[i] + nums[j] > t:
                    j -= 1
                elif nums[i] + nums[j] < t:
                    i += 1
                elif nums[i] + nums[j] == t:
                    op.add((nums[z], nums[i], nums[j]))
                    i += 1
        return op