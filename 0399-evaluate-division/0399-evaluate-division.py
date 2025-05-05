from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        
        for i in range(len(equations)):
            adj[equations[i][0]].append((equations[i][1], values[i]))
            adj[equations[i][1]].append((equations[i][0], 1 / values[i]))
        
        def dfs(src, dst):
            if src not in adj or dst not in adj:
                return -1
            
            q = deque([(src, 1)])
            visited = set()

            while q:
                source, weight = q.popleft()
                if source == dst:
                    return weight
                
                for nei, wei in adj[source]:
                    if nei not in visited:
                        q.append((nei, weight * wei))
                        visited.add(nei)
            return -1 
        
        return [dfs(q[0], q[1]) for q in queries]