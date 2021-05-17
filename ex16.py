# Exercise 16

#like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"first: {arg1}, second: {arg2}")

# *args was unecessary, try this
def print_two_again(arg1, arg2):
    print(f"first: {arg1}, second: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("Eric", "Moyer")
print_two_again("Eric", "Moyer")
print_one("ONE!")
print_none()
