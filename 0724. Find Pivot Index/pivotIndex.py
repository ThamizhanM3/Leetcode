class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = 0
        a = []
        b = []
        for i in nums:
            s += i
            a.append(s)
        nums = nums[::-1]
        s = 0
        for i in nums:
            s += i
            b.append(s)
        b = b[::-1]
        for i in range(len(nums)):
            if a[i] == b[i]:
                return i
        return -1