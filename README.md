# Greedy-and-dynamic-programming
School project. Not complete


# IKT301 Greedy and dynamic programming
Date due: See Canvas 
## Make the necessary assumptions (which may include reducing the size of the data). 
For the first and second problems, use the Basic World Cities Database. It can be downloaded for free here: https://simplemaps.com/data/world-cities.
For the third and fourth problems, there is no need for external data. 
For the fifth problem, use the P08 dataset from John Burkart. It can be downloaded for free here: https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html. 

## Problem 1. Travelling Salesperson (TSP)
Use the longitude and latitude from the Norwegian cities from the Basic World Cities database, calculate the distance, and find the shortest path visiting all cities using:1.   Dynamic programming2.   Greedy
## Problem 2. Minimum spanning tree
Use the distances calculated from problem 1, and choose a subset of the Norwegian cities to create a minimum spanning tree using:1.   Prim’s algorithm2.   Kruskal’s algorithm 
## Problem 3. Huffman coding
In this assignment, you should make a lossless compressor using Huffman coding. Make an application that can take as input an arbitrary text consisting of the 29 Norwegian characters and compress the text using:1.   Huffman coding with fixed-length encoding2.   Huffman coding with variable size encodingThe compressed text should include the characters (assume ASCII), codes, and the message.
## Problem 4. Job scheduling
Generate a random dataset with at least 50 jobs. Each job should have a profit and a deadline no later than 40. Find the maximum profit under the constraints of the deadlines for all jobs. Problem 5. KnapsackUse the weights, profits, and knapsack capacity from the P08 dataset to find the optimal packing in two ways:1.   With the fractional knapsack problem2.   With the binary (0/1) knapsack problem
