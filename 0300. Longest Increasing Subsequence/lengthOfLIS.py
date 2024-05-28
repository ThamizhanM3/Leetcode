class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        for i in range(len(dp)-1, -1, -1):
            z = [0]
            for j in range(i+1, len(dp)):
                if nums[i] < nums[j]:
                    z.append(dp[j])
            dp[i] = 1+max(z)
        print(dp)
        return max(dp)



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        for i in range(len(dp)-1, -1, -1):
            z = 0
            for j in range(i+1, len(dp)):
                if nums[i] < nums[j]:
                    z = max(z, dp[j])
            dp[i] = 1+z
        return max(dp)



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        for i in range(len(dp)-1, -1, -1):
            z = [0]
            for j in range(i+1, len(dp)):
                if nums[i] < nums[j]:
                    z.append(dp[j])
            dp[i] = 1+max(z)
        return max(dp)