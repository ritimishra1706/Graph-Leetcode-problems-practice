class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        q=[]
        status=set()
        adj=[[]for i in range(n)]
        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)
        c=0    
        for i in range(n):
            if i not in status:
                status.add(i)
                q.append(i)
                c+=1
                while q:
                    x=q.pop(0)
                    for i in adj[x]:
                        if i not in status:
                            status.add(i)
                            q.append(i)
        return c-1                    
                    





        