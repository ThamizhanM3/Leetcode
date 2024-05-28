class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(permutations(nums))


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        x = permutations(nums)
        y = []
        for i in x:
            if i not in y:
                y.append(i)
        return y