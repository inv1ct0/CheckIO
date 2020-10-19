def is_all_upper(text: str) -> bool:
    if len(text) == 0:
        print("len is zero")
        return True
    text_without_space = text.split()
    text_without_space = "".join(text_without_space)
    print(text_without_space)
    if not text_without_space.isalpha():
        print("is not alpha")
        return True
    for char in text_without_space:
        if not char.isupper():
            print("char is lower")
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
