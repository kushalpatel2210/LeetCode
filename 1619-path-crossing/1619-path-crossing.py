class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = [(0, 0)]
        newDir = None

        for direction in path:
            x, y = visited[-1][0], visited[-1][1]
            
            if direction == 'N':
                newDir = (x, y + 1)
            elif direction == 'S':
                newDir = (x, y - 1)
            elif direction == 'E':
                newDir = (x + 1, y)
            else:
                newDir = (x - 1, y)
            
            if newDir in visited:
                return True
            visited.append(newDir)
        
        return False