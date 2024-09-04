class Solution:
    def __init__(self):
        self.a = []

    def check(self, i, a):
        a.append(i)
        if i == len(self.graph)-1:
            self.a.append(a)
        for j in self.graph[i]:
            self.check(j, a.copy())
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.check(0, [])
        return self.a