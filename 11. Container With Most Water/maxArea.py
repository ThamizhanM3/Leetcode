class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        m = 0
        while i < j:
            c = min(height[i], height[j]) * (j-i)
            if m < c:
                m = c
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m