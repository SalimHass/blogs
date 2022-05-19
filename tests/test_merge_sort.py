from blogs.merge_sort.merge_sort import merge_sort
import pytest

def test_merge_sort1():
    actual = [4, 8, 15, 16, 23, 42]
    expexted= merge_sort([8,4,23,42,16,15])
    assert expexted==actual

def test_merge_sort2():
    actual = [-2, 5, 8, 12, 18, 20]
    expexted= merge_sort([20,18,12,8,5,-2])
    assert expexted==actual

def test_merge_sort3():
    actual = [5, 5, 5, 7, 7, 12]
    expexted= merge_sort([5,12,7,5,5,7])
    assert expexted==actual

def test_merge_sort4():
    actual =  [2, 3, 5, 7, 11, 13]
    expexted= merge_sort([2,3,5,7,13,11])
    assert expexted==actual

def test_merge_sort_empty():
    with pytest.raises(Exception):
        merge_sort([])


def test_merge_sort_none():
    with pytest.raises(Exception):
        merge_sort()

