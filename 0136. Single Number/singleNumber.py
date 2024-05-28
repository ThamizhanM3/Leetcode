class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = Counter(nums)
        for i in a.items():
            if i[1] == 1:
                return i[0]