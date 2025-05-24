from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_to_y = defaultdict(list)
        y_to_x = defaultdict(list)
        count = 0

        for x, y in buildings:
            x_to_y[x].append(y)
            y_to_x[y].append(x)

        for x in x_to_y:
            x_to_y[x].sort()
        
        for y in y_to_x:
            y_to_x[y].sort()      

        for x, y in buildings:
            horizontalBuildings = y_to_x[y]
            verticalBuildings = x_to_y[x]

            if horizontalBuildings[0] < x < horizontalBuildings[-1] and verticalBuildings[0] < y < verticalBuildings[-1]:
                count += 1
        
        return count