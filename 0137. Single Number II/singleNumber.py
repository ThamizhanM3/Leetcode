class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = Counter(nums).items()
        for i in x:
            if i[1] == 1:
                return i[0]