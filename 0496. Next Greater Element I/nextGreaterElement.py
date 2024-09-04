class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            j = nums2.index(i)
            x = -1
            k = j
            while j < len(nums2):
                if nums2[j] > nums2[k]:
                    x = nums2[j]
                    break
                j += 1
            ans.append(x)
        return ans