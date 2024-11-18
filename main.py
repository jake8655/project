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


arr = [random.randint(1, 100) for _ in range(10)]


print(
    """Help:
x = exit
n = new
p = print
o = remove last
z = remove first"""
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

# Add to the beginning
# Remove from the beginning
# Add anywhere
# Remove from anywhere
