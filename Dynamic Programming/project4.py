"""
Math 560
Project 4
Fall 2020

Author: Suqian Wang
Date: Nov 6, 2020
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
PATH: the function that return an optimal set of edits
INPUTS: 
dir_table - a matching DP table shows the dependency how each cell calculated
src: the original string
dest: the target string
OUTPUTS:
a list of edits, each edit is a 3-tuple showing what operation was performed on which char
and the index of this edit in the original string
"""
def PATH(dir_table, src, dest):
    # initialization
    m = len(src)
    n = len(dest)
    edits = []
    i = m
    j = n

    # backward updating the edits
    # 'L' - insertion, go to the cell to the left
    # 'U'  - deletion, go to the cell to the top
    # 'DM'/'DS' - match/substitution, go to the adjacent cell to the upper left
    while(1):
        if dir_table[i][j] == 'L':
            edits.append(['insert', dest[j-1], i])
            j -= 1
        elif dir_table[i][j] == 'U':
            edits.append(['delete', src[i-1], i-1])
            i -= 1
        elif dir_table[i][j] == 'DM':
            edits.append(['match', dest[j-1], i-1])
            i -= 1
            j -= 1
        elif dir_table[i][j] == 'DS':
            edits.append(['sub', dest[j-1], i-1])
            i -= 1
            j -= 1
        else: 
            return  edits


                            
"""
ED: the edit distance function
"""
def ED(src, dest):
    # initialization
    dist = 0
    edits = []
    m = len(src)
    n = len(dest)
    dp_table = [[0 for i in range(n+1)] for j in range(m+1)]
    dir_table = [[0 for i in range(n+1)] for j in range(m+1)]
    # base case: initilize the first row and first column in the DP table and the direction table
    for i in range(1, m+1):
        dp_table[i][0] = i
        dir_table[i][0] = 'U'
    for j in range(1, n+1):
        dp_table[0][j] = j
        dir_table[0][j] = 'L'
    
    # Loop thru the table row by row
    for i in range(1, m+1):
        for j in range(1, n+1):
            # if the char in the original and target string are the same
            # no change to edit distance
            # indicate it is a match in the direction table
            if src[i-1]  == dest[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1]
                dir_table[i][j] = 'DM'
            # if the char in the original and target string are different
            # select the best strategy(smallest edit distance) from insertion, deletion and substitution
            # add one edit to distance
            # indicate the correspond edit in the direction table
            else:
                insert = dp_table[i][j-1]
                delete = dp_table[i-1][j]
                sub = dp_table[i-1][j-1]
                best_strat = min(insert, delete, sub)
                dp_table[i][j] = 1 + best_strat
                if best_strat == sub:
                    dir_table[i][j] = 'DS'
                elif best_strat == insert:
                    dir_table[i][j] = 'L'
                else:
                    dir_table[i][j] = 'U'
    # the result is the last cell in the DP table
    dist = dp_table[m][n]
    edits = PATH(dir_table, src, dest)
    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300)
    print()
    compareRandStrings(True, 30, 300)
