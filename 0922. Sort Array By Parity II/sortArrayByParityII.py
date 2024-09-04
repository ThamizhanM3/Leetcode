class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ev = []
        od = []
        n = len(nums)
        for i in nums:
            ev.append(i) if i%2 == 0 else od.append(i)
        op = []
        for i in range(n//2):
            op.append(ev.pop(0))
            op.append(od.pop(0))
        return op



class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ev = []
        od = []
        n = len(nums)
        for i in nums:
            ev.append(i) if i%2 == 0 else od.append(i)
        op = []
        for i in range(n):
            op.append(ev.pop(0)) if i%2 == 0 else op.append(od.pop(0))
        return op