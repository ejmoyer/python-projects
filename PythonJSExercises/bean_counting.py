def count_bs(arg):
    result = 0
    string = len(arg)
    for i in range(0, string):
        if arg[i] == "B":
            result += 1

    return result
#print(count_bs('BBC'))

# countchar
def count_char(arg, char):
    result = 0
    string = len(arg)
    for i in range(0, string):
        if arg[i] == str(char):
            result += 1

    return result
print(count_char('kakkerlak', 'k'))
