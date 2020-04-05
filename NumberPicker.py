from random import randint
from random import seed
import time
from tabulate import tabulate


# Initialize the board
DrawnNumbers = [""] * 76

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def PickNumber (DrawnNumbers):
    seed(time.time())
    while True:
        pick = randint(1, 75)
        if DrawnNumbers[pick] == "":
            DrawnNumbers[pick] = pick
            break
    
    if pick <= 15:
        letter = "B"
    elif pick <= 30:
        letter = "I"
    elif pick <= 45:
        letter = "N"
    elif pick <= 60:
        letter = "G"
    else:
        letter = "O"

    print('The next number is {}{}'.format(letter, pick))
    print("")
    print("")
    DisplayPickedNumbers (DrawnNumbers)
    return DrawnNumbers

def DisplayPickedNumbers (DrawnNumbers):
    table = []
    for i in range (1, 16):
        table.append([DrawnNumbers[i], DrawnNumbers[i + 15], DrawnNumbers[i + 30], DrawnNumbers[i + 45], DrawnNumbers[i + 60]])

    print(tabulate(table, headers=["B", "I", "N", "G", "O"]))

def GeneratePlayerCard():
    while True:
        BoardSeed = input("Please Enter the board ID number:  ")
        if RepresentsInt(BoardSeed):
            BoardSeed = int(BoardSeed)
            break
        else:
            print("You didn't enter a valid number.  Please Try again.")

    board = []
    for i in range (5):
        board.append([""] * 5)
    seed(BoardSeed)

    board = FillNumbers(board, 0, 1, 15)
    board = FillNumbers(board, 1, 16, 30)
    board = FillNumbers(board, 2, 31, 45)
    board = FillNumbers(board, 3, 46, 60)
    board = FillNumbers(board, 4, 61, 75)
    return board

def FillNumbers(board, Col, Low, High):
    values = []
    for i in range (5):
        while True:
            value = randint(Low,High)
            if not(value in values):
                values.append(value)
                break
        board[i][Col] = str(value)
    return board


def CheckBingo(DrawnNumbers):
    board = GeneratePlayerCard()
    for i in range (5):
        for j in range (5):
            if int(board[i][j]) in DrawnNumbers:
                board[i][j] = "XX"
    board[2][2] = "XX"
    print(tabulate(board, headers=["B", "I", "N", "G", "O"]))


# Main program loop
while True:
    print("Please select an option!")
    print("1.  Draw a number")
    print("2.  Check a BINGO")
    print("3.  Exit")
    print("")
    selection = input("Enter your choice:  ")

    if selection == "1":
        PickNumber (DrawnNumbers)
    elif selection == "2":
        CheckBingo(DrawnNumbers)
        answer = input("Was there a bingo?  ")
        if (answer == "y") or (answer == "Y"):
            break
    elif selection == "3":
        break
    else:
        print("That is not a valid option, try again")
