class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            for j in range(i+1, n):
                if x == nums[j]:
                    return [i, j]

sol = Solution()

inp1 = [
    [2,7,11,15],
    [3,2,4],
    [3,3]
]

inp2 = [
    9,
    6,
    6
]

for i in range(len(inp1)):
    print(sol.twoSum(inp1[i], inp2[i]))