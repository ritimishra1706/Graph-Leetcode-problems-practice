class Solution:
    # USING BFS
    def numSquares(self, n: int) -> int:
        q=[]
        # sum and count
        q.append([0,0])
        visit=[0]*(n+1)
        visit[0]=1
        
        while q:
            s,count=q.pop(0) 
            for i in range(1,int(math.sqrt(n))+1):
                if s+i*i==n:
                    return count+1
                s1=s+i*i    
                if s1<n and visit[s1]==0:
                    c=count+1
                    q.append([s1,c])
                    visit[s1]=1
                    
    


            
        