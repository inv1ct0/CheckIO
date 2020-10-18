def nearest_value(values: set, one: int) -> int:
    list_values = list(values)
    list_values.sort()
    if one in values:
        return int(one)
    if int(one) == 0 and int(list_values[0]) > 0:
        return int(list_values[0])
    if int(one) > int(list_values[len(list_values)-1]):
        return int(list_values[len(list_values)-1])
    for num in range(len(list_values) - 1):
        if int(list_values[num]) < one < int(list_values[num+1]):
            if (one - int(list_values[num])) < (int(list_values[num+1]) - one):
                return int(list_values[num])
            elif (one - int(list_values[num])) > (int(list_values[num+1]) - one):
                return int(list_values[num+1])
            else:
                return int(list_values[num])


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
