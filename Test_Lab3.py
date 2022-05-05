import Lab3

print("Test_Lab3")


def test_bubble_lessten_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 2)

def test_bubble_lessten_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 2)

def test_bubble_moreten_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 21, 77, 89, 100]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)

def test_bubble_moreten_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 21, 77, 89, 100]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 1)

def test_bubble_zero_invalid():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)

def test_bubble_ten_ascending():
    result = []
    input_arr = [54, 43, 32, 21, 19, 67, 78, 98, 86, 1]
    test_arr = [1, 19, 21, 32, 43, 54, 67, 78, 86, 98]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_ten_descending():
    result = []
    input_arr = [54, 43, 32, 21, 19, 67, 78, 98, 86, 1]
    test_arr = [98, 86, 78, 67, 54, 43, 32, 21, 19, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_nonint_descending():
    result = []
    input_arr = ["a", 43.2, 32, 21, 19, 67, 78, 98, 86, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 3)

def test_bubble_nonint_ascending():
    result = []
    input_arr = ["a", 43.2, 32, 21, 19, 67, 78, 98, 86, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 3)
