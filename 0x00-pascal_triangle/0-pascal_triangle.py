#!/usr/bin/python3
"""
pascal_triangle - returns a list of lists of integers representing the Pascal’s triangle of n
"""
def pascal_triangle(n):
    """
    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: Pascal's triangle represented as a list of lists.
    """
    if(n == 0):
        return []
    listoflists = [[1]]
    for i in range(1, n):
        previous_row = listoflists[i -1]
        new_row = [1] + [previous_row[j-1] + previous_row[j] for j in range(1, i)] + [1]
        listoflists.append(new_row)
    return listoflists            

