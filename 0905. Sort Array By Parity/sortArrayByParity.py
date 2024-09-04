class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        b = []
        for i in nums:
            b.append(i) if i%2 != 0 else b.insert(0, i)
        return b