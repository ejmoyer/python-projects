result = ''
for y in range(0, 8):
    for x in range(0, 8):
        if (x + y) % 2 != 0:
            result += "#"
        else:
            result += " "
    result += "\n"
print(result)
