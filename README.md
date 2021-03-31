# Algorithms
This repository contains five coding based mini-projects from which I implemented and exploited different sorting algorithms, BFS and DFS algorithms, Bellman-Ford algorithm, edit distance algorithm, Prim’s algorithm and Kruskal algorithm. 

Each folder has a detailed description describe the project and the files that are needed.

## Sorting: Time Complexity
In this project, I implemented a number of sorting algorithms such as Selection Sort, Insertion Sort, Bubble Sort, Merge Sort, and Quick Sort. I compared the runtime of these different sorting algorithms on random and sorted arrays. The detailed report of this project can be found in the corresponding folder.

## DFS & BFS: Maze Solving
In this project, I implemented a Stack and a Queue class with the basic functions of a stack/queue data structure such as push, pop, resize, and check if it is empty or full. I also implemented the DFS and BFS algorithms using the stack and queue data structure to solve several different mazes (2D array) that were represented by adjacency lists.

## Bellman-Ford: Arbitrage Detection
Arbitrage is the strategy of taking advantage of price differences in different markets for the same asset. When we encode the currencies exchange as a graph (adjacency matrix), arbitrage would be a cycle of currencies where their exchange rate multiplication is greater than 1. In other words, arbitrage detection is finding a negative cost cycle of currencies where the cost between currencies is the negative log value of exchange rate. In this project, I implemented the Bellman-Ford algorithm with an error tolerance to detect a negative cost cycle (arbitrage) from the currencies exchange graph. 

## Dynamic Programming: Edit Distance
Edit distance is the least number of edits (insertion, deletion, substitution) required to convert one string to another. In this project, I implemented a dynamic programming approach to the edit distance problem, and reconstructed an optimal set of edits using the dynamic programming table.

## MST: Traveling Salesman Problem
In this project, I implemented the Prim’s and Kruskal algorithms to find minimum spanning trees in the graph where cities are the vertices and the edge weights are given as the distance between all the pairs of cities. Then I use depth first search from the start city in the graph and traverse the minimum spanning tree, and since it is the minimum spanning tree, the result will be the lowest cost tour.
