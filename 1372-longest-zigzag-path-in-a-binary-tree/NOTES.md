**We have given a set of nodes with their level of traversal where null denotes no path, we have to find the longest length of zig zag traversal of edges.**
We need to store total length and direction for every node we are visiting, it decides, what is the next move in either left or right direction.
1. right indicates 2, left=1.
2. but if not started yet, so will start by assigning current dircetion to 1 for left visiting.,
3.  if at the starting if we have  not a left node , we will start by assignig current direction to       for right viisting.
4. And if we are not at right path we are not increasing our total distance only moving with the help of 1 and 2.