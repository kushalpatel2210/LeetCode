from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, eq in enumerate(equations):
            adj[eq[0]].append((eq[1], values[i]))
            adj[eq[1]].append((eq[0], 1 / values[i]))
        
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
                        q.append([nei, wei * weight])
                        visited.add(nei)

            return -1

        return [dfs(s, d) for s, d in queries]