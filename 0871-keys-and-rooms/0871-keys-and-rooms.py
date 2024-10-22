class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:  
        visited = set()

        def dfs(graph, start):
            visited.add(start)

            for neighbor in graph[start]:
                if neighbor not in visited:
                    dfs(graph, neighbor)
        
            for vertice in range(len(graph)):
                if vertice not in visited:
                    return False
        
            return True
        
        return dfs(rooms, 0)