class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,j,n):
            if n==len(word):
                return True
            if i<0 or  i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[n]:
                return False
            temp=board[i][j]
            board[i][j]=''
            if backtrack(i+1,j,n+1) or backtrack(i-1,j,n+1) or backtrack(i,j+1,n+1) or backtrack(i,j-1,n+1):
                return True
            board[i][j]=temp
            return False
        for  i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False                      
        