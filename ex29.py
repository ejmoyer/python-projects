# ex 29

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Chair", "Frisbee",
                "Avocados", "Kiwi", "Wallaby", "Corn"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)
print("Let's don some things with stuff.")

print(stuff[1])
print(stuff[-1]) #the last thing in a list, negatives start from the end
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5])) ## 3:5 is a range of indexes
#:3 shows all but the third index and beyond
#1: shows all but the first index
