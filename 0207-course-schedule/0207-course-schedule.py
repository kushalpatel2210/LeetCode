from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        schedule = defaultdict(list) # Preq, course
        coursesTaken = 0
        inDegree = [0] * numCourses

        for crs, preq in prerequisites:
            schedule[preq].append(crs)
            inDegree[crs] += 1
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:
            currCrs = q.popleft()
            coursesTaken += 1

            for crs in schedule[currCrs]:
                inDegree[crs] -= 1

                if inDegree[crs] == 0:
                    q.append(crs)
        
        return coursesTaken == numCourses
