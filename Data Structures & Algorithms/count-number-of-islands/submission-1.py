class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        def bfs(i,j):
            grid[i][j]='0'
            q=[]
            q.append([i,j])
            while q:
                nq=[]
                while q:
                    x,y=q.pop()
                    for dx,dy in d:
                        nx=x+dx
                        ny=y+dy
                        if nx>-1 and ny>-1 and nx<n and ny<m and grid[nx][ny]=='1':
                            nq.append([nx,ny])
                            grid[nx][ny]='0'
                q=nq
        ans=0
        for x in range(n):
            for y in range(m):
                if grid[x][y]=='1':
                    ans+=1
                    bfs(x,y)
        return ans