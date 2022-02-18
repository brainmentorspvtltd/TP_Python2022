positions = [i for i in range(1,10)]
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
    pass

def cpuMove(choice):
    pass

def main():
    gameBoard()
    userChoice = input("Enter your choice : X | 0 : ")
    if userChoice == "X":
        cpuChoice = "0"
    else:
        cpuChoice = "X"

    userMove(userChoice)
    gameBoard()

    cpuMove(cpuChoice)
    gameBoard()

main()
