# Topological Sort
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        courses = defaultdict(list)
        inDegree = [0] * numCourses
        res = []

        for crs, preq in prerequisites:
            courses[crs].append(preq)
            inDegree[preq] += 1
        
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)
        
        coursesTaken = 0

        while q:
            currCrs = q.popleft()
            res.append(currCrs)
            coursesTaken += 1

            for course in courses[currCrs]:
                inDegree[course] -= 1

                if inDegree[course] == 0:
                    q.append(course)

        return res[::-1] if coursesTaken == numCourses else []