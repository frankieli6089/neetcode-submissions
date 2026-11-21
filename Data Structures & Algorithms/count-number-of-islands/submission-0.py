from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #keeps track of whether the node was found as part of an island 
        # 1 means yes, we skip
        # 2 means no, we must perform BFS on this node
        def bfs(i, j, visited):
            q = deque()
            
            if (j-1 >= 0 and grid[i][j-1] == "1" and visited[(i, j-1)] == 0):
                q.append((i, j-1))
                visited[(i, j-1)] = 1
            if (j+1 < len(grid[i]) and grid[i][j+1] == "1" and visited[(i, j+1)] == 0):
                q.append((i, j+1))
                visited[(i, j+1)] = 1
            if (i-1 >= 0 and grid[i-1][j] == "1" and visited[(i-1, j)] == 0):
                q.append((i-1, j))
                visited[(i-1, j)] = 1
            if (i+1 < len(grid) and grid[i+1][j] == "1" and visited[(i+1, j)] == 0):
                q.append((i+1, j))
                visited[(i+1, j)] = 1
           
            while len(q) > 0:
                coords = q.popleft()
                curr_i, curr_j = coords
                if curr_j - 1 >= 0:
                    if grid[curr_i][curr_j - 1] == "1" and visited[(curr_i, curr_j - 1)] == 0:
                        q.append((curr_i, curr_j - 1))
                        visited[(curr_i, curr_j - 1)] = 1

                if curr_j + 1 < len(grid[0]):
                    if grid[curr_i][curr_j + 1] == "1" and visited[(curr_i, curr_j + 1)] == 0:
                        q.append((curr_i, curr_j + 1))
                        visited[(curr_i, curr_j + 1)] = 1

                if curr_i - 1 >= 0:
                    if grid[curr_i - 1][curr_j] == "1" and visited[(curr_i - 1, curr_j)] == 0:
                        q.append((curr_i - 1, curr_j))
                        visited[(curr_i - 1, curr_j)] = 1

                if curr_i + 1 < len(grid):
                    if grid[curr_i + 1][curr_j] == "1" and visited[(curr_i + 1, curr_j)] == 0:
                        q.append((curr_i + 1, curr_j))
                        visited[(curr_i + 1, curr_j)] = 1

        total_islands = 0
        visited = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                visited[(i, j)] = 0
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[(i, j)] == 1:
                    continue
                if grid[i][j] == "0":
                    continue

                if grid[i][j] == "1":
                    visited[(i, j)] = 1
                    bfs(i, j, visited)
                    total_islands += 1
        
        return total_islands
                
                