class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        o = []
        for i in nums1:
            if i in nums2:
                nums2.pop(nums2.index(i))
                o.append(i)
        return o