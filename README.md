# Algorithms-4th-Edition
Course material of Coursera https://www.coursera.org/learn/algorithms-part1/

## Union-Find


**Question : Social network connectivity. Given a social network containing n members and a log file containing m timestamps at which times pairs of members formed friendships,design an algorithm to determine the earliest time at which all members are connected (i.e., every member is a friend of a friend of a friend . . . . . . . of a friend). Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. The running time of your algorithm should be m log n or better and use extra space proportional to n.**

Answer
1. We can keep track of a new variable called `connected_components` which will keep track of the connected components at current time.
2. On each union we'll update the connected components as required.
3. On each union operation we'll check it's value.
4. When `connected_components` = 1 that timestamp in log will be the earliest time when all members were connected.

**Question : Union-find with specific canonical element. Add a method find() to the union-find data type so that find(i) returns the largest element in the connected component containing i. The operations, union(), connected(), and find() should all take logarithmic time or better. For example, if one of the connected components is {1,2,6,9}, then the find() method should return 9 for each of the four elements in the connected components.**

Answer
1. We'll maintain one more array for `highs`, which will have keep track of the largest element in the component at root. 
2. We'll update the value on each union at root.
3. For find operation we need to check the value at `highs` root index that will be the highest value in component.

**Question : Successor with delete. Given a set of n integers S={0,1,...,n−1} and a sequence of requests of the following form:
		a. Remove x from S
		b. Find the successor of x: the smallest y in S such that y ≥ x.
		c. design a data type so that all operations (except construction) take logarithmic time or better in the worst case.**

Answer
1. We can use the Union find approach to keep track of the removed elements and highest.
2. Connect the neighbor elements if not connected already. 
3. In addition to that we can use above approach for find() which will always keep track of the highest element in component connected

- [x] Percolation Excercise - 100/100
