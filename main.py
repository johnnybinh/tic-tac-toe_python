from os import system, name
from array import *


# print
def printArr(arr):
    clear()
    print("-----------")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            match arr[i][j]:
                case 0:
                    print("|O|", end=" ")
                case 1:
                    print("|X|", end=" ")
                case " ":
                    print("| |", end=" ")
        print("\n-----------\n")


# clear
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def arrModifier():
    x, y = [int(x) for x in input("X turn: \n").split()]
    arr[x - 1][y - 1] = 1
    printArr(arr)
    x, y = [int(x) for x in input("O turn: \n").split()]
    arr[x - 1][y - 1] = 0


# map
rowMoves = int()
colMoves = int()
rows, cows = (3, 3)
arr = [
    [" "] * cows for _ in range(rows)
]  # this list is independent. authur need to google


# main loop
while 1:
    # printArr
    printArr(arr)
    arrModifier()
    clear()
