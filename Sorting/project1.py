"""
Math 560
Project 1
Fall 2020

Author: Suqian Wang
Date: Oct 9, 2020
"""

"""
Swap Funtion

This function will swap the two elements in a list

INPUTS: 
listToSwap: the original list
i, j: two indices of the list

OUTPUTS:
a new list with the element at index i swapped with the element at index j
"""
def swap(listToSwap, i, j):
    temp = listToSwap[i]
    listToSwap[i] = listToSwap[j]
    listToSwap[j] = temp

"""
SelectionSort

Each iteration, this function will select the smallest element in the unsorted portion of the list,
and insert that element in the sorted portion of the list

INPUTS:
listToSort: the original list(could be unsorted or sorted)

OUTPUTS:
listTosort: sorted list
"""
def SelectionSort(listToSort):

    for pointer in range(len(listToSort)):
        min_index = pointer

        # find the smallest elements in the rest of the list
        for i in range(pointer+1,len(listToSort)):
            if(listToSort[i] < listToSort[min_index]):
                min_index = i

        # swap the smallest element with the first unsorted element
        swap(listToSort, pointer, min_index)

    return listToSort

"""
InsertionSort

Each iteration, this function will select the first element in the unsorted portion of the list,
and bubble that element forward until it is in a sorted position in the sorted portion of the list

INPUTS:
listToSort: the original list(could be unsorted or sorted)

OUTPUTS:
listTosort: sorted list
"""
def InsertionSort(listToSort):

    for i in range(1, len(listToSort)):
        elem_to_insert = listToSort[i]

        # compare the element to sort with the one in front, swap if order is reversed
        j = i-1
        while j >= 0:
            if elem_to_insert < listToSort[j]:
                swap(listToSort, j, j+1)
                j -= 1
            if elem_to_insert >= listToSort[j]:
                break

    return listToSort

"""
BubbleSort

This function will compare each pair of adjacent element in the list and order them if necessary.
The elements after the last swapped position of the previous iteration will be already sorted.
There is a flag that indicate whether a iteration has elements that got swapped or not.
If there is no elements got swapped, the list is sorted.

INPUTS:
listToSort: the original list(could be unsorted or sorted)

OUTPUTS:
listTosort: sorted list
"""
def BubbleSort(listToSort):

    for i in range(len(listToSort)):
        is_swap = False

        for j in range(0, len(listToSort)-i-1):
            if listToSort[j] > listToSort[j+1]:
                swap(listToSort, j, j+1)
                is_swap = True

        if is_swap == False:
            break

    return listToSort

"""
MergeSort

This function break the list in half and recursively sort each half,
and eventually combine the sorted half back by traversing the two halves simultaneously
and inserted the elements in order in the list

INPUTS:
listToSort: the original list(could be unsorted or sorted)

OUTPUTS:
listTosort: sorted list
"""
def MergeSort(listToSort):

    n = len(listToSort)

    # single element, no need to sort, just return
    if n <= 1:
        return listToSort
    
    # two elements, swap if necessary
    if n == 2:
        if listToSort[0] > listToSort[1]:
            swap(listToSort, 0, 1)
        return listToSort

    # choose the middle element and recursively call MergeSort on the left and right half
    mid_index = n//2
    left_array = MergeSort(listToSort[:mid_index])
    right_array = MergeSort(listToSort[mid_index:])

    # merge the sorted left and right half
    l = 0
    r = 0
    for i in range(n):

        # when the left and right array pointer both hasn't reach the end
        # insert the smaller value to the list and move that pointer forward
        if l < len(left_array) and r < len(right_array):       
            if left_array[l] < right_array[r]:
                listToSort[i] = left_array[l]
                l += 1
            else:
                listToSort[i] = right_array[r]
                r += 1

        # when the left array pointer reached the end, insert the rest of the right array in the list
        elif l == len(left_array) and r < len(right_array):
            listToSort[i] = right_array[r]
            r += 1

        # when the right array pointer reached the end, insert the rest of the left array in the list
        elif r == len(right_array) and l < len(left_array):
            listToSort[i] = left_array[l]
            l += 1

    return listToSort

"""
partition

This function takes a list and partition the list into two by a specified pivot value.
After the partition, one list should have values that are no greater than the pivot value,
and the other list should have values that are no less than the pivot value

INPUTS:
listToPartition: the original list
p: a pivot value
left_pointer: the left most index of the list
right_pointer: the right most index of the list

OUTPUTS:
left_pointer: the left most index of a sublist where its elements are no less than the pivot value
right_pointer: the right most index of a sublist where its elements are no greater than the pivot value
"""
def partition(listToPartition, left_pointer, right_pointer, p):
    while left_pointer <= right_pointer:

        # if the left pointer element is smaller than the pivot, keep moving the left pointer to the right
        while left_pointer <= right_pointer and listToPartition[left_pointer] < p:
            left_pointer += 1

        # if the right pointer element is bigger than the pivot, keep moving the right pointer to the left
        while left_pointer <= right_pointer and listToPartition[right_pointer] > p:
            right_pointer -= 1

        # when the left and right pointer stucked, swap the element and move both pointer
        if left_pointer <= right_pointer:
            swap(listToPartition, left_pointer, right_pointer)
            left_pointer += 1
            right_pointer -= 1

    return left_pointer, right_pointer

"""
QuickSort
This function recursively select the middle of a list as the piviot value, 
and partition the list using the partition function until eventually all the partitions are sorted

INPUTS:
listToSort: the original list(could be unsorted or sorted)
i: the first index of the list
j: the last index + 1 of the list

OUTPUTS:
listTosort: sorted list

"""
def QuickSort(listToSort, i=0, j=None):

    # Set default value for j if None.
    if j == None:
        j = len(listToSort)

    # list is invalid or single element
    if i >= j:
        return listToSort

    l = i
    r = j-1

    # choose the middle element as pivot
    p = listToSort[(l+r)//2]

    l, r = partition(listToSort, l, r, p)

    QuickSort(listToSort, i, r+1)
    QuickSort(listToSort, l, j)

    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    print("\n------>Measuring time when list is presorted...")
    measureTime(preSorted = True)
    print("\n------>Measuring time when list is randomized...")
    measureTime()
    
