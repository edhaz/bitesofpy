def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    string_list = list(string)
    return "".join(string_list[n:] + string_list[:n])

