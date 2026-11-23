from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def bfs(i, j):
            total_area = 1
            q = deque()
            q.append((i, j))

            while len(q) > 0:
                i, j = q.popleft()
                if (i-1 >= 0 and grid[i-1][j] == 1 and (i-1, j) not in visited):
                    q.append((i-1,j))
                    visited.add((i-1,j))
                    total_area += 1 
                if (i+1 < len(grid) and grid[i+1][j] == 1 and (i+1, j) not in visited):
                    q.append((i+1,j))
                    visited.add((i+1,j))
                    total_area += 1 
                if (j-1 >= 0 and grid[i][j-1] == 1 and (i, j-1) not in visited):
                    q.append((i,j-1))
                    visited.add((i,j-1))
                    total_area += 1 
                if (j+1 < len(grid[0]) and grid[i][j+1] == 1 and (i, j+1) not in visited):
                    q.append((i,j+1))
                    visited.add((i,j+1))
                    total_area += 1 

            return total_area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1 and (i, j) not in visited):
                    visited.add((i, j))
                    val = bfs(i, j)
                    if val > max_area:
                        max_area = val
        
        return max_area
