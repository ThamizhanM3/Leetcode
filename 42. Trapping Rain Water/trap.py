class Solution:
    def trap(self, height: List[int]) -> int:
        lm = [height[0]]
        for i in height[1:]:
            lm.append(max(lm[-1], i))
        rm = [height[-1]]
        for i in height[::-1][1:]:
            rm.append(max(rm[-1], i))
        rm = rm[::-1]
        s = 0
        for i in range(len(height)):
            s += min(lm[i], rm[i]) - height[i]
        return s