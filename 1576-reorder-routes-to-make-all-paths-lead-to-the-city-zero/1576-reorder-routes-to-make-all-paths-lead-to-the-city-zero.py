from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        edges = set()
        visited = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
            edges.add((a, b))
        
        def dfs(city):
            nonlocal changes

            visited.add(city)
            for neighbor in neighbors[city]:
                if neighbor not in visited:
                    if (neighbor, city) not in edges:
                        changes += 1
                    dfs(neighbor)
        
        dfs(0)
        
        return changes
