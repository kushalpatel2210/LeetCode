class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
        province = 0
        visited = set()

        def dfs(city):
            visited.add(city)
            # Traverse the neighbors of the current city
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
            
        for city in range(len(isConnected)):
            if city not in visited:
                # Found a new province, start a DFS and increment the count
                dfs(city)
                province += 1
        
        return province