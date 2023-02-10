def reverse(string):
    if not string:
        return string

    return reverse(string[1:]) + string[0]
