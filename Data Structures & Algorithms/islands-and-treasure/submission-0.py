class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n=len(grid)
        m=len(grid[0])
        d=[[0,1],[1,0],[0,-1],[-1,0]]

        def bfs(i,j):
            q=[[i,j]]
            visited=set()
            visited.add((i,j))
            dist=0
            while q:
                nq=[]
                dist+=1
                while q:
                    r,c=q.pop(0)
                    for dr,dc in d:
                        nr=r+dr
                        nc=c+dc
                        if 0<=nr<n and 0<=nc<m and grid[nr][nc]>0 and (nr,nc) not in visited:
                            visited.add((nr,nc))
                            grid[nr][nc]=min(grid[nr][nc],dist)
                            nq.append([nr,nc])
                q=nq
        for i in range(n):
            for j in range(m):
                if not grid[i][j]:
                    bfs(i,j)
