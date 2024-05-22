class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # time complexity for first transpose part
        # O(n/2 * n/2)
        # for reverse : O(n/2)

        for i in range(len(matrix)-1):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]    
                 
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        