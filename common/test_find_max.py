#from find_max import find_max


def test_find_max(list1):
    """
    Checks if the number real max number in a list
    """
    max = list1[0]

    for x in list1:
        if x > max: # comparing the list
          max = x

    return max


list1 = [2, 0, 30, 55, 60, -66]
print("max number is:", test_find_max(list1))
