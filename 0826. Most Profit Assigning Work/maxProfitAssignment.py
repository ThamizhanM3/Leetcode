class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difpro = sorted(zip(profit, difficulty))
        difpro = sorted(difpro, reverse = True)
        worker = sorted(worker, reverse = True)
        p = 0
        j = 0
        for i in worker:
            while j < len(difpro):
                if i >= difpro[j][1]:
                    p += difpro[j][0]
                    break
                j += 1
        return p



class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difpro = [[profit[i], difficulty[i]] for i in range(len(profit))]
        difpro = sorted(difpro, reverse = True)
        p = 0
        for i in worker:
            for j in difpro:
                if i >= j[1]:
                    p += j[0]
                    break
        return p