class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        opt = []
        x = Counter(nums).items()
        for i in x:
            if i[1] == 1:
                opt.append(i[0])
        return opt