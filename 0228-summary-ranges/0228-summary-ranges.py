class Solution:
    # using two sets, one for storing state of an element and other for searching in the set
    # searching in set takes o(1) constant time
    # s2  stores if any consecutive element present in nums, so dont need to traverse
    # last range would be our last consecutive element of that range.
    def summaryRanges(self, nums: List[int]) -> List[str]:
        s=set(nums)
        s2=set()
        l=[]
        start=""
        end=""
        for i in nums:
            if i in s2:
                continue
            s2.add(i)    
            a=i+1
            start+=str(i)
            while a in s:
                s2.add(a)
                a+=1
            end+=str(a-1)
            if start==end:
                l.append(start)
            else:
                l.append(start+"->"+end)
            start=""
            end=""   
        return l         
             


