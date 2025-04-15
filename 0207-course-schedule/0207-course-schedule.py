# Topological Sort
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses) }
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            indegree[pre] += 1

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for pre in preMap[node]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        
        return finish == numCourses

'''
# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}
        visitSet = set()

        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
'''