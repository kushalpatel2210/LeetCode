# Topological sort 
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        schedule = defaultdict(list)
        inDegree = [0] * numCourses
        q = deque()

        for crs, preq in prerequisites:
            schedule[crs].append(preq)
            inDegree[preq] += 1
        
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)
        
        coursesTaken = 0
        while q:
            node = q.popleft()
            coursesTaken += 1

            for crs in schedule[node]:
                inDegree[crs] -= 1

                if inDegree[crs] == 0:
                    q.append(crs)
        
        return coursesTaken == numCourses