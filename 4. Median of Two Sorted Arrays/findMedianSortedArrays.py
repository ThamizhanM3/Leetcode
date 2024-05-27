class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = []
        i, j = 0, 0
        m = len(nums1)
        n = len(nums2)
        for k in range(m+n):
            if i >= m:
                a += nums2[j:]
            elif j >= n:
                a += nums1[i:]
            elif nums1[i] < nums2[j]:
                a.append(nums1[i])
                i += 1
            else:
                a.append(nums2[j])
                j += 1
        print(a)
        if (m+n) % 2:
            return (a[(m+n)//2]*10)/10
        else:
            return (a[(m+n)//2]+a[((m+n)//2)-1])/2