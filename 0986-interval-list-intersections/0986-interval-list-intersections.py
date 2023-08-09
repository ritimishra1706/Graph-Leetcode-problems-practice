class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        ans=[]
        while i<len(firstList) and j<len(secondList):
            s=max(firstList[i][0],secondList[j][0])
            e=min(firstList[i][1],secondList[j][1])
            # if only overlaps, if does not valid like [2,5],[6,8] this does not overlap 
            if s<=e:
                ans.append([s,e])
            # because it will not overlap again, we choosen overlapped part earlier    
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1   
        return ans             