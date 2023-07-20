#User function Template for python3

def reverseWord(s):
    i=0
    j=len(s)-1
    l=list(s)
    while i<j:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
    return "".join(l)    
        
    #your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends