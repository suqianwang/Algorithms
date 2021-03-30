"""
Math 560
Project 3
Fall 2020

Author: Suqian Wang
Date: Oct 29, 2020
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    # initialize distances and previous nodes
    for v in adjList:
        v.dist = math.inf
        v.prev = None
    
    # initialize start vertex
    start = adjList[0]
    start.dist = 0
    
    neg = False
    last = start
    # iterate |V| - 1 times 
    for i in range(0, len(adjList)-1):
        # look at each vertex
        for u in adjList:
            # check each neighbor of u, update predictions and previous vertex if necessary
            for neigh in u.neigh:
                if neigh.dist > u.dist + adjMat[u.rank][neigh.rank] + tol:
                    neigh.dist = u.dist + adjMat[u.rank][neigh.rank]
                    neigh.prev = u
    
    # loop one more to detect negative cost cycles
    for u in adjList:
        # if negative cycle found, break out of the loop
        if neg:
            break
        # check each neighbor of u, if one needs to update its distance, a negative cycle is found
        for neigh in u.neigh:
            if neigh.dist > u.dist + adjMat[u.rank][neigh.rank] + tol:
                neg = True
                neigh.prev = u
                last = neigh
                break
            last = neigh
    
    if neg:
        path = list()
        
        # retrace path
        while last != None:
            if last.rank in path:
                path.append(last.rank)
                break
            path.append(last.rank)
            last = last.prev

        # reverse path to correct order
        path = path[::-1]

        path_dict = dict()
        # find repeated element and return cycle
        for index,value in enumerate(path):
            if(path_dict.get(value) != None):
                return path[path_dict.get(value):index+1]
            else:
                path_dict[value] = index
    else:
        # return empty list for no cycles
        return []

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    return [[-math.log(R) for R in row] for row in rates]

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
    
