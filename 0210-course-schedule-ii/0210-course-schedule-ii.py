# DFS

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i: [] for i in range(numCourses) }
        visitSet, cycle = set(), set()
        res = []

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visitSet:
                return True

            cycle.add(crs)
            visitSet.add(crs)

            for nei in adj[crs]:
                if not dfs(nei):
                    return False

            res.append(crs)
            cycle.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
        



'''
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
        
'''
        