class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [1]
        rp = [1]
        x = 1
        for i in nums[:-1]:
            lp.append(i*lp[-1])
        x = 1
        for i in nums[::-1][:-1]:
            rp.append(i*rp[-1])
        rp = rp[::-1]
        op = []
        i = 0
        for i in range(len(rp)):
            op.append(lp[i]*rp[i])
        return op