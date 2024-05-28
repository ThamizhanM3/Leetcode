class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        c = x.most_common()
        op = []
        for i in range(k):
            op.append(c[i][0])
        return op