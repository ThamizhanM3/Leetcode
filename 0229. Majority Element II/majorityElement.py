class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        n = len(nums)/3
        a = []
        for i in x.items():
            if int(i[1]) > n:
                a.append(i[0])
        return a