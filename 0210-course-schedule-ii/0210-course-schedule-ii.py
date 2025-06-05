from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        schedule = defaultdict(list)
        inDegree = [0] * numCourses
        completedCourses = 0
        q = deque()
        res = []

        for crs, preq in prerequisites:
            schedule[preq].append(crs)
            inDegree[crs] += 1
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        while q:
            crs = q.popleft()
            completedCourses += 1
            res.append(crs)

            for course in schedule[crs]:
                inDegree[course] -= 1
                
                if inDegree[course] == 0:
                    q.append(course)
        
        return res if completedCourses == numCourses else []
