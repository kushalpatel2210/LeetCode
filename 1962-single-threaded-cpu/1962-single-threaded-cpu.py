import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        available = []
        pending = []
        result = []

        for i, (enqueueTime, processingTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processingTime, i))


        while available or pending:
            while pending and pending[0][0] <= time:
                enqueueTime, processingTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processingTime, i))
            
            if not available:
                time = pending[0][0]
                continue
            
            processTime, i = heapq.heappop(available)
            time += processTime
            result.append(i)
        
        return result

    
        
        

