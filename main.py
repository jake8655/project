import random


def intInput(text: str = "number: "):
    a = input(text)
    num = None
    while num == None:
        try:
            num = int(a)
        except:
            a = input(text)
    return num


def ask_for_new_num(arr: list[int]):
    new = intInput()
    arr.append(new)


def remove_last(arr: list[int]):
    if len(arr) == 0:
        print("im empty dumbass")
        return

    arr.pop()


def remove_first(arr: list[int]):
    if len(arr) == 0:
        print("im empty dumbass")
        return

    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr.pop()


def add_first(arr: list[int]):
    # loop from end to start (exclusive)
    for i in range(len(arr) - 1, 0, -1):
        # at the end append element to the list and set the previous last element to the one before it
        if i == len(arr) - 1:
            curr = arr[i]
            arr[i] = arr[i - 1]
            arr.append(curr)
            continue
        arr[i] = arr[i - 1]

    new = intInput()
    arr[0] = new


def remove_anywhere(arr: list[int]):
    idx = intInput("index: ")
    # make sure idx is valid according to the list
    while idx < 0 or idx > len(arr) - 1:
        idx = intInput()

    # Loop from index (inclusive) to penultimate element
    for i in range(idx, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()


arr = [random.randint(1, 100) for _ in range(10)]


print(
    """Help:
x = exit
n = new
p = print
o = remove last
z = remove first
a = add first
r = remove anywhere"""
)

command: str = ""
while command != "x":
    print(arr)
    command = input()

    if command == "n":
        ask_for_new_num(arr)
    if command == "p":
        print(arr)
    if command == "o":
        remove_last(arr)
    if command == "z":
        remove_first(arr)
    if command == "a":
        add_first(arr)
    if command == "r":
        remove_anywhere(arr)

# Add to the beginning ✅
# Remove from the beginning ✅
# Add anywhere
# Remove from anywhere ✅
