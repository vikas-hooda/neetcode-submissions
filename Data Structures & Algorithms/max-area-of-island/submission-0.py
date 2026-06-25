class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(i,j):
            ans=1
            grid[i][j]=0
            for dx,dy in d:
                x=i+dx
                y=j+dy
                if x>-1 and y>-1 and x<n and y<m and grid[x][y]:
                    ans+=dfs(x,y)
            return ans
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ans=max(ans,dfs(i,j))
        return ans