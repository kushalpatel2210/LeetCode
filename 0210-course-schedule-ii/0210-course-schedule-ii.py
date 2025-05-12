from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        q = deque()
        inDegree = [0] * numCourses 
        seq = list()

        for crs, preq in prerequisites:
            preMap[crs].append(preq)
            inDegree[preq] += 1
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        processed = 0
        while q:
            node = q.popleft()
            seq.append(node)
            processed += 1

            for preq in preMap[node]:
                inDegree[preq] -= 1

                if inDegree[preq] == 0:
                    q.append(preq)
        
        return [] if processed != numCourses else seq[::-1]