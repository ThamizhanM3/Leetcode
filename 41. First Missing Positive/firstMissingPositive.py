class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a = [i for i in nums if i > 0]
        a = list(set(a))
        a.sort()
        if len(a) == 0:
            a.append(0)
        print(a)
        for i in range(len(a)):
            if i+1 != a[i]:
                return i+1
        return len(a)+1