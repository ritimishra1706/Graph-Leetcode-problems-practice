class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # simple dfs ,if we check one string to another,based on only two mismatced character
        # that matching string will be my neighbour of current node
        # if it is not visited, mark it visit
        def issimilar(s1,s2):
            count=0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    count+=1
            if count==0 or count==2:
                return True
            else:
                return False            



        def dfs(Sourcenodeindex,visited,strs):
            visited[Sourcenodeindex]=1
            for j in range(len(strs)):
                if visited[j]==1:
                    continue
                if issimilar(strs[Sourcenodeindex],strs[j]):
                    dfs(j,visited,strs)
        

        visited=[0]*len(strs)
        component=0 #no.of groups
        for i in range(len(strs)):
            if visited[i]==0:         
                component+=1
                dfs(i,visited,strs) # exactly called c times(c = no.of connected components)
        return component        

