"""
Math 560
Project 5
Fall 2020

Author: Suqian Wang
Date: Nov 21, 2020
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm: this function track the minimum cost edge leading out of the current tree
INPUTS:
adjList: the adjacency list for the map
adjMat: the adjacency matrix for the map

OUTPUT: None
"""
def prim(adjList, adjMat):
    # initialize all vertices costs to infinity and their previous vertex is null
    for v in adjList:
        v.cost = math.inf
        v.prev = None
        v.visited = False
    
    # pick an arbitrary start vertex and set cost to 0
    start = adjList[0]
    start.cost = 0

    # make the priority queue for vertices
    Q = PriorityQueue()
    for v in adjList:
        Q.insert(v)

    while not Q.isEmpty():
        # Get the next unvisited vertex and visit it
        v = Q.deleteMin()
        v.visited = True

        # Loop thru each edge out of that vertex
        for nbr in v.neigh:
            # if it has not been visited, update the cost to the smallist edge weight
            if not nbr.visited:
                if nbr.cost > adjMat[v.rank][nbr.rank]:
                    nbr.cost =  adjMat[v.rank][nbr.rank]
                    nbr.prev = v
    return

################################################################################

"""
Kruskal's Algorithm: find the minimum cost edge, add it to the MST if it does not produce a cycle

INPUTS:
adjList: the adjacency list for the map
edgeList: list of already sorted edges in the map

OUTPUTS:
X: the list of edges in MST
"""
def kruskal(adjList, edgeList):
    # initialize all singleton sets for each vertex
    for v in adjList:
        makeset(v)

    # initialize the empty MST
    X = []

    # loop through the edges in increasing order
    for e in edgeList:
        # if the min edge crosses a cut, add it to our MST
        u, v = e.vertices
        if not find(u).isEqual(find(v)):
            X.append(e)
            union(u, v)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    # if we are not at the root
    if v != v.pi:
        # set our parent to be the root
        v.pi = find(v.pi)
    # return our parent/root
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    # find the root of the tree
    ru = find(u)
    rv = find(v)

    # if the sets are the same, return
    if ru == rv:
        return

    # shorter set point to taller set, union tree height don't change
    # same height, union tree height increment 1
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height: 
        ru.pi = rv
    else:
        ru.pi = rv
        rv.height += 1
    return

################################################################################

"""
TSP: this function will trace the TSP tour(minimize the cost of the tour) using depth first search on the MST

INPUTS:
adjList: The adjacency list for the map
start: starting vertex

OUTPUTS:
tour: a list of connected vertices with minimum traveling cost
"""
def tsp(adjList, start):
    # initialize the tour
    tour = []
    
    # initialize all vertices
    for v in adjList:
        v.visited = False

    # initialize a stack
    stack = []
    stack.append(start)
    
    # while the stack is not empty
    while len(stack) != 0:
        curr = stack.pop()
        # skipping the city visited
        if curr.visited == False:
            curr.visited = True
            # appending new visited vertex to the tour
            tour.append(curr.rank)
            # check the neighbors in the MST
            for nbr in curr.mstN:
                stack.append(nbr)
    
    # tour end at the start vertex to complete cycle
    tour.append(start.rank)
    return tour

# def tsp(adjList, start):
#     # initialize the tour
#     tour = []
    
#     # initialize all vertices
#     for v in adjList:
#         v.visited = False

#     # initialize a stack
#     stack = []
    
#     # visit the first city and mark it on the tour
#     start.visited = True
#     stack.append(start)
#     tour.append(start.rank)
    
#     # while the stack is not empty
#     while len(stack) != 0:
#         curr = stack.pop()
#         # visit the unvisited city on the MST and mark them on the tour
#         for nbr in curr.mstN:
#             if nbr.visited == False:
#                 nbr.visited = True
#                 stack.append(nbr)
#                 tour.append(nbr.rank)
    
#     # tour end at the start vertex to complete cycle
#     tour.append(start.rank)
#     return tour
################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
