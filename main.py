import random


def intInput():
    a = input("number: ")
    num = None
    while num == None:
        try:
            num = int(a)
        except:
            a = input("number: ")
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
    # loop from end to start
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


arr = [random.randint(1, 100) for _ in range(10)]


print(
    """Help:
x = exit
n = new
p = print
o = remove last
z = remove first
a = add first"""
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

# Add to the beginning ✅
# Remove from the beginning ✅
# Add anywhere
# Remove from anywhere
