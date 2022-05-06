import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 200, 300]
    test_arr = [11, 12, 22, 25, 34, 64, 90, 100, 200, 300]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 200, 300]
    test_arr = [300, 200, 100, 90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)


def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 200, 300]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_less():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_n = 2
    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == test_n )

def test_bubble_sort_more():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 200, 300, 4]
    test_n = 1
    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == test_n)

def test_bubble_sort_0():
    result = []
    input_arr = []
    test_n = 0
    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == test_n)

def test_bubble_sort_not_int():
    result = []
    input_arr = [64, 34, 25, "12", 22, 11, 90]
    test_n = 3
    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == test_n)