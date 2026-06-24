class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j):
            dx=[0,1,0,-1]
            dy=[1,0,-1,0]
            grid[i][j]='0'
            for k in range(4):
                x=i+dx[k]
                y=j+dy[k]
                if x>-1 and y>-1 and x<n and y<m:
                    if grid[x][y]=='1':
                        dfs(x,y)
        ans=0
        for x in range(n):
            for y in range(m):
                if grid[x][y]=='1':
                    ans+=1
                    dfs(x,y)
        return ans