class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # USING BFS for shortest path
        visited=[[0 for i in range(len(grid))]for j in range(len(grid))]
        if grid[0][0]!=0:
            return -1
        queue=[]
        direction=[[0,-1],[-1,0],[0,1],[1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        queue.append([0,0,1])
        visited[0][0]=1
        while queue:
            x,y,path_len=queue.pop(0)
            if x==len(grid)-1 and y==len(grid)-1:
                return path_len 
            for i,j in direction:
                new_r=x+i
                new_col=y+j
                if new_r>=0 and new_col>=0 and new_r<len(grid) and new_col<len(grid[0]) and grid[new_r][new_col]==0 and visited[new_r][new_col]==0:
                    visited[new_r][new_col]=1
                    queue.append([new_r,new_col,path_len+1])
        return -1            
            

        