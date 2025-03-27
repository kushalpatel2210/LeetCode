class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        # directed graph
        for i in range(len(equations)):
            adj[equations[i][0]].append((equations[i][1], values[i])) # dest, weight
            adj[equations[i][1]].append((equations[i][0], 1 / values[i]))
        
        def bfs(src, dest):
            if src not in adj or dest not in adj:
                return -1
            
            q = deque([(src, 1)])
            visited = set()

            while q:
                node, w = q.popleft()
                if node == dest:
                    return w
                
                for nei, weight in adj[node]:
                    if nei not in visited:
                        q.append((nei, w * weight))
                        visited.add(nei)
            return -1 

        return [bfs(q[0], q[1]) for q in queries] 