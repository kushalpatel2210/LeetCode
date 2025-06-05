from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        schedule = defaultdict(list)
        inDegree = [0] * numCourses 
        q = deque()
        coursesTaken = 0

        for crs, preq in prerequisites:
            schedule[preq].append(crs)
            inDegree[crs] += 1
            
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:
            crs = q.popleft()
            coursesTaken += 1

            for course in schedule[crs]:
                inDegree[course] -= 1

                if inDegree[course] == 0:
                    q.append(course)
        
        return coursesTaken == numCourses