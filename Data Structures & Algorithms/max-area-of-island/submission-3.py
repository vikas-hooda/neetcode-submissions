class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        def bfs(i,j):
            ans=0
            q=[[i,j]]
            grid[i][j]=0
            while q:
                r,c=q.pop(0)
                ans+=1
                for dx , dy in d:
                    nr=r+dx
                    nc=c+dy
                    if nr>-1 and nc>-1 and nr<n and nc<m and grid[nr][nc]:
                        q.append([nr,nc])
                        grid[nr][nc]=0
            return ans
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ans=max(ans,bfs(i,j))
        return ans