class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j,visited,grid,q):
            q.append([i,j])
            visited[i][j]=1
            direction=[[0,1],[1,0],[-1,0],[0,-1]]
            while q:
                x,y=q.popleft()
                for i,j in direction:  
                        new_r=x+i
                        new_col=y+j
                        if new_r>=0 and new_r<len(grid) and new_col>=0 and new_col<len(grid[0]) and  grid[new_r][new_col]=="1" and visited[new_r][new_col]==0:
                            visited[new_r][new_col]=1
                            q.append([new_r,new_col])
                                           
        ans=0
        n=len(grid)
        m=len(grid[0])
        visited=[[0 for i in range(m)]for j in range(n)]
        q=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and visited[i][j]==0:
                    ans+=1
                    bfs(i,j,visited[:],grid,q)
            

                
        return ans
        
        