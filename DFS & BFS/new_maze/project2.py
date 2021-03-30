"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1:
Partner 2:
Date:
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    # choose data structure based on alg
    data_struc = None
    if(alg == 'BFS'):
        data_struc = Queue()
    else:
        data_struc = Stack()
    # initialize all vertices, they have not been visited and have no previous node
    for vertex in maze.adjList:
        vertex.visited = False
        vertex.prev = None
    # visit starting vertex and push it into stack/queue
    start = maze.start
    start.visited = True
    data_struc.push(start)
    # while the stack/queue not empty (there are vertices left to visit)
    curr = None
    while not data_struc.isEmpty():
        curr = data_struc.pop()
        # find the exit
        if curr == maze.exit:
            break
        # visit the neighbors if necessary and push it into stack/queue
        for n in curr.neigh:
            if(n.visited):
                continue
            else:
                n.visited = True
                data_struc.push(n)
                n.prev = curr
    # derive path backwards from the exit vertex
    path = list()
    while(curr != None):
        path.append(curr.rank)
        curr = curr.prev
    
    # reverse the list so the path is in correct order from start to exit vertex
    maze.path = path[::-1]
    return maze.path

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
