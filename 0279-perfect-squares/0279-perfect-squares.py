class Solution:
    def numSquares(self, n: int) -> int:
        k=int(math.sqrt(n))
        # column is sum, row is square roots
        dp=[[0 for i in range(n+1)]for j in range(k)]
        for i in range(n+1):
            dp[0][i]=i
        for i in range(1,k):
            for j in range(1,n+1):
                sq=(i+1)*(i+1)
                if sq>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    # min(previous count if not using current perfect square,
                    # (j//sq)--> how many times we can use current perfect square
                    # [j%sq]--> which perfect square need for remaining sum)
                    dp[i][j]=min(dp[i-1][j],(j//sq)+dp[i][j%sq])
        return dp[-1][-1]                    

        