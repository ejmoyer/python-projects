# Exercise 19

def add():
    print("Add?")
    a = int(input())
    print("and?")
    b = int(input())
    print(f"ADDING {a} + {b}")
    return a + b

def subtract():
    print("Subtract?")
    a = int(input())
    print("And?")
    b = int(input())
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply():
    print("Multiply?")
    a = int(input())
    print("And?")
    b = int(input())
    print(f"MULTIPLAYING {a} * {b}")
    return a * b

def divide():
    print("Divide?")
    a = int(input())
    print("And?")
    b = int(input())
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with functions")

age = add()
height = subtract()
weight = multiply()
iq = divide()

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#can you do it by hand?
#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#print("That becomes: ", what, ". Did you figure it out?")
