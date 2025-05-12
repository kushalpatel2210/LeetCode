from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        inDegree = [0] * numCourses
        q = deque()

        for crs, prq in prerequisites:
            preMap[crs].append(prq)
            inDegree[prq] += 1

        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)
        
        courses = 0
        while q:
            node = q.popleft()
            courses += 1

            for prq in preMap[node]:
                inDegree[prq] -= 1

                if inDegree[prq] == 0:
                    q.append(prq)

        return courses == numCourses