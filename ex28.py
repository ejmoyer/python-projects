# ex 28
def loop_while(arg, inc):
    numbers = []

    for i in range(0, arg, inc):
        print(f"At the top i is {i}")

        numbers.append(i)
        print(f"Numbers now: {numbers}")

        print(f"At the bottom i is {i}")
    print(numbers)
    return numbers

print("The number:")

for num in loop_while(8, 2):
    print(num)
