# DAG - Topological Sort
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i: [] for i in range(numCourses) }
        indegree = [0] * numCourses
        res = []

        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        processed = 0
        while q:
            node = q.popleft()
            res.append(node)
            processed += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return [] if processed != numCourses else res[::-1]
        