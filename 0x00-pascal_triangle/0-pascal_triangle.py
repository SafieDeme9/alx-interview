#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: Pascal's triangle represented as a list of lists.
    """
    if (n <= 0):
        return []
    listoflists = [[1]]
    for i in range(1, n):
        row = listoflists[i - 1]
        newrow = [1] + [row[j-1] + row[j] for j in range(1, i)] + [1]
        listoflists.append(newrow)
    return listoflists
