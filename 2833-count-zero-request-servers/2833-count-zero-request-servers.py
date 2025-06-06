# Sweeping Line
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x: x[1]) # sort logs by time
        indexed_queries = sorted([(time, i) for i, time in enumerate(queries)])
        left = right = 0
        server_req_count = defaultdict(int)
        unique_active_servers = set()
        res = [0] * len(queries)

        for query_time, i in indexed_queries:
            while right < len(logs) and logs[right][1] <= query_time:
                server_id = logs[right][0]
                server_req_count[server_id] += 1
                unique_active_servers.add(server_id)
                right += 1
            
            while left < len(logs) and logs[left][1] < query_time - x:
                server_id = logs[left][0]
                server_req_count[server_id] -= 1
                if server_req_count[server_id] == 0:
                    unique_active_servers.remove(server_id)
                left += 1
            
            not_active_servers = n - len(unique_active_servers)
            res[i] = not_active_servers
        
        return res

