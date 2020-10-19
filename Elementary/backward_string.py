def backward_string(val: str) -> str:
    # или
    # print("".join(reversed(val)))

    # или
    # chars = list(val)
    # for i in range(len(val) // 2):
    #     tmp = chars[i]
    #     chars[i] = chars[len(val) - i - 1]
    #     chars[len(val) - i - 1] = tmp
    # return ''.join(chars)

    return val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
