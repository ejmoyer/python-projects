# return arg % 2 == 0
def is_even(arg):
    if arg == 0:
        return True
    elif arg == 1:
        return False
    else:
        return is_even(arg - 2)
print(is_even(50))
