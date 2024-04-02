class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue=deque()
        queue.append([sr,sc])
        col1=image[sr][sc]
        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        if image[sr][sc]==color:
            return image
        while queue:
            x,y=queue.popleft()
            image[x][y]=color    
            for i,j in direction:
                new_r=i+x
                new_c=y+j
                if new_r>=0 and new_c>=0 and new_r<len(image) and new_c<len(image[0]) and image[new_r][new_c]==col1:
                    image[new_r][new_c]=color
                    queue.append([new_r,new_c])   
        return image             
        