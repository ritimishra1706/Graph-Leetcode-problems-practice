**Intution:**
​
Every time we have to search consecutive elements for a starting value and for constant time searching, I used set, and the last consecutive element is the end range. We also need one more set to set status of visited elements. I learnt this idea by solving similar problem : longest consecutive sum in optimized manner by Striver at Youtube and tried to apply it here.
​
**Approach:**
​
Here, I used two sets: **s1, s2**. s1 is for searching next consecutive element in constant time.For every element in nums, we are storing start range and we are finding the next consecutive of that element until sequence breaks, the last element of the sequence will be our **end range**. We don't need to revisit those elements which are covered in a range, so I used **s2** set for storing status of visited elements.And at the last we just append our start and end range in a list, by checking if our end range and start range is equal, so just append only one as it is single element and for others store both ranges.
Set empty to both string start and end range for storing next ranges. Return the answer list l.
​
**Time complexity**: O(n)*k k is the number of set of ranges
**Space complexity**: O(n)+O(n)=O(n)
​