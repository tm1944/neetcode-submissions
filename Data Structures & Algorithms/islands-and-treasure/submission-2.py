class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid),len(grid[0])
        visited = set()
        q = deque()

        def addCopy(r,c):
            if(
                r < 0 or c < 0 or r == ROWS or c == COLS or 
                grid[r][c] == -1 or (r,c) in visited
            ):
                return
            visited.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])
        
        dist = 0
        while q:
            qlen = len(q)
            for _ in range(qlen):
                r,c = q.popleft()
                grid[r][c] = dist
                addCopy(r+1,c)
                addCopy(r-1,c)
                addCopy(r,c+1)
                addCopy(r,c-1)
            dist+=1
