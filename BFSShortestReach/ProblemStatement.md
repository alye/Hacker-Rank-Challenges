Problem description taken from: 
https://www.hackerrank.com/challenges/bfsshortreach

Consider an undirected graph consisting of *n* nodes where each node is labeled from *1* to *n* and the edge between any two nodes is always of length 6. 
We define node *s* to be the starting position for a BFS.

Given *q* queries in the form of a graph and some starting node, *s*, perform each query by calculating the shortest distance from starting node *s* to all the other nodes in the graph. Then print a single line of *n-1* space-separated integers listing node *s*'s shortest distance to each of the *n-1* other nodes (ordered sequentially by node number); if *s* is disconnected from a node, print -1 as the distance to that node.

###Input Format

The first line contains an integer,*q* , denoting the number of queries. The subsequent lines describe each query in the following format:

- The first line contains two space-separated integers describing the respective values of *n* (the number of nodes) and *m* (the number of edges) in the graph.
- Each line *i* of the  subsequent lines contains two space-separated integers, *u* and *v*, describing an edge connecting node *u* to node *v*.
- The last line contains a single integer, *s*, denoting the index of the starting node.
 
###Constraints

- 1 <= *q* <= 10
- 2 <= *n* <= 1000
- 1 <= *u*,*v*,*s* <=n
- 1 <= *m* <= *n*.(*n*-1)/2

###Output Format

For each of the  queries, print a single line of  space-separated integers denoting the shortest distances to each of the  other nodes from starting position . These distances should be listed sequentially by node number (i.e., ), but should not include node . If some node is unreachable from , print  as the distance to that node.

###Sample Input
```
2
4 2
1 2
1 3
1
3 1
2 3
2
```

###Sample Output
```
6 6 -1
-1 6
```