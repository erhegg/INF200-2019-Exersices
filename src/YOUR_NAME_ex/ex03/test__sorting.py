# -*- coding: utf-8 -*-

__author__ = 'Erik Heggelund'
__email__ = 'erhe@nmbu.no'


def bubble_sort(list_to_be_sorted):
    """The function takes a list or tuple and sorts it with the bubble sort
    method. The function returns the sorted list or tuple as a tuple.
    """
    sorted_list = list(list_to_be_sorted)
    for iteration_number in range(1, len(list_to_be_sorted)):
        for index in range(len(sorted_list[:-iteration_number])):
            if sorted_list[index] > sorted_list[index + 1]:
                sorted_list[index], sorted_list[index + 1] = (
                    sorted_list[index + 1],
                    sorted_list[index],
                )
            else:
                pass
    return tuple(sorted_list)


def test_empty():
    """Test that the sorting function works for empty list"""
    data = []
    assert bubble_sort(data) == data


def test_single():
    """Test that the sorting function works for single-element list"""
    assert len(bubble_sort([1])) == 1
    assert bubble_sort([1]) == 1


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    pass


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    pass


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    pass


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    pass


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    pass


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass
