class Solution:
    def check(self, i):
        for j in self.rooms[i]:
            if not self.visited[j]:
                self.visited[j] = True
                self.check(j)
                
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = [False for i in rooms]
        self.rooms = rooms
        self.visited[0] = True
        self.check(0)
        return len(rooms) == sum(self.visited)