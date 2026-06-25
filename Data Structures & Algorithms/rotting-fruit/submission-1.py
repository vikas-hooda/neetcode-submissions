class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans=0
        n=len(grid)
        m=len(grid[0])
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        q=[]
        visited=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append([i,j])
                    visited.add((i,j))
        while q:
            ans+=1
            nq=[]
            while q:
                r,c=q.pop(0)
                for dr,dc in d:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<n and 0<=nc<m and (nr,nc) not in visited and grid[nr][nc]==1:
                        nq.append([nr,nc])
                        grid[nr][nc]=2
                        visited.add((nr,nc))
            q=nq
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return max(ans-1,0)