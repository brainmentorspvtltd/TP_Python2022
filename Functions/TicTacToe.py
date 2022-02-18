import random

positions = [i for i in range(1,10)]
occupied = []
def gameBoard():
    print("""
    {}  |  {}  |  {}
    --------------
    {}  |  {}  |  {}
    --------------
    {}  |  {}  |  {}
    """.format(positions[0], positions[1], positions[2],
               positions[3], positions[4], positions[5],
               positions[6], positions[7], positions[8]))

def checkWinner():
    pass

def userMove(choice):
    pos = int(input("Enter the position : "))
    positions[pos - 1] = choice
    occupied.append(pos)
    checkWinner()

def cpuMove(choice):
    pos = random.randint(1,9)
    if pos in occupied:
        print("Already Occupied :",pos)
        cpuMove(choice)
    else:
        print("CPU Moved at :",pos)
        positions[pos - 1] = choice
        occupied.append(pos)
        checkWinner()

def main():
    gameBoard()
    userChoice = input("Enter your choice : X | 0 : ")
    if userChoice == "X":
        cpuChoice = "0"
    else:
        cpuChoice = "X"

    game = True
    while game:
        userMove(userChoice)
        gameBoard()

        cpuMove(cpuChoice)
        gameBoard()

main()
