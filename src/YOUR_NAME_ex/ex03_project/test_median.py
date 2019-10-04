# -*- coding: utf-8 -*-

__author__ = 'Erik Heggelund'
__email__ = 'erhe@nmbu.no'

import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    if len(data) < 1:
        raise ValueError('The list cannot be empty')
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_single():
    """Test that the median function works for single-element list"""
    data = [1]
    assert median(data) == data[0]
    assert median(data) == 1


def test_odd_number_elements():
    """Test that checks that the correct median is returned for
    lists with odd numbers of elements"""
    data = [1, 57, 2, 1, 345]
    assert median(data) == 2


def test_even_number_elements():
    """Test that checks that the correct median is returned for
    lists with even numbers of elements"""
    data = [123, 43, 5, 7, 12, 0]
    assert median(data) == 0.5*(7+12)


def test_ordered_list():
    """Test that checks that the correct median is returned for
    lists with ordered elements"""
    data = [1, 2, 3, 4, 5, 6, 7]
    assert median(data) == 4


def test_reverse_ordered_list():
    """Test that checks that the correct median is returned for
    lists with reverse ordered elements"""
    data = [7, 6, 5, 4, 3, 2, 1]
    assert median(data) == 4


def test_unordered_elementss():
    """Test that checks that the correct median is returned for
    lists with unordered elements"""
    data = [1235634532, 3, 1, 34, 765, 87653, 0.0000005]
    assert median(data) == 34


def test_empty_list():
    """Test that the median function raises ValueError for empty list"""
    with pytest.raises(ValueError):
        median([])


def test_original_unchanged():
    """Test that median leaves the original data unchanged"""
    data = [3, 5, 1, 24, 5, 5.0]
    median(data)
    assert data == [3, 5, 1, 24, 5, 5.0]


def test_median_of_tuple():
    """Test that the median function also works for tuple"""
    data = (1, 4, 2, 7)
    assert median(data) == 3
