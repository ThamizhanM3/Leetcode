class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 1
        v = nums[0]
        for i in nums[1:]:
            if v == i:
                c += 1
            else:
                c -= 1
                if c == 0:
                    v = i
                    c = 1
        return v



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = Counter(nums)
        a = a.most_common()
        return a[0][0]



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = set(nums)
        n = len(nums)
        b = []
        for i in a:
            b.append([nums.count(i), i])
        b = sorted(b, reverse = True)
        return b[0][1]