class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(root,adj,visited):
            visited[root]=1
            for i in adj[root]:
                if visited[i]==0:
                    dfs(i,adj,visited)
        n=len(isConnected)
        adj=[[]for i in range(n+1)]
        for i in range(n):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1:
                    adj[i].append(j)
                    adj[j].append(i)
        visited=[0]*n
        c=0
        for i in range(n):
            if visited[i]==0:
                c+=1
                dfs(i,adj,visited)  
        return c                  
                   
