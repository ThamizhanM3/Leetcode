class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key = len)
        if strs[0] == "":
            return ""
        for ind in range(len(strs[0])):
            for i in strs:
                if strs[0][ind] != i[ind]:
                    return strs[0][:ind]
        return strs[0]


class Solution:
    def longestCommonPrefix(self, strs):
        pre = strs[0]
        npre = ""
        for i in strs:
            for j in range(min(len(pre), len(i))):
                if pre[j] == i[j]:
                    npre += pre[j]
                else:
                    break
            pre = npre
            npre = ""
        return pre