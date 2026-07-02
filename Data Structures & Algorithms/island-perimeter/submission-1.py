class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=set()
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        C=len(grid[0])
        R=len(grid)
        def cs(i,j):
            ans=0
            for dx,dy in d:
                ni=i+dx
                nj=j+dy
                if 0>ni or ni==R or nj<0 or nj==C or grid[ni][nj]==0:
                    ans+=1
            return ans
        def bfs(i,j,visited):
            visited.add((i,j))
            ans=0
            q=[(i,j)]
            while q:
                r,c=q.pop(0)
                
                ans+=cs(r,c)
                for dx,dy in d:
                    nr=r+dx
                    nc=c+dy
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc] and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            return ans
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    return bfs(i,j,visited)