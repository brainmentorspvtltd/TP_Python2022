import random

winning_combinations = [[1,2,3],[4,5,6],[7,8,9],
					    [1,4,7],[2,5,8],[3,6,9],
						[1,5,9],[3,5,7]]

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

def checkWinner(pos, choice):
    for i in range(len(winning_combinations)):
        if pos in winning_combinations[i]:
            index = winning_combinations[i].index(pos)
            winning_combinations[i][index] = choice

    # print(winning_combinations)
    for i in range(len(winning_combinations)):
        c1 = winning_combinations[i][0] == choice
        c2 = winning_combinations[i][1] == choice
        c3 = winning_combinations[i][2] == choice
        if c1 and c2 and c3:
            return "winner"


def userMove(choice):
    pos = int(input("Enter the position : "))
    positions[pos - 1] = choice
    occupied.append(pos)
    return checkWinner(pos, choice)

def cpuMove(choice):
    pos = random.randint(1,9)
    if pos in occupied:
        print("Already Occupied :",pos)
        cpuMove(choice)
    else:
        print("CPU Moved at :",pos)
        positions[pos - 1] = choice
        occupied.append(pos)
        return checkWinner(pos, choice)

def main():
    gameBoard()
    userChoice = input("Enter your choice : X | 0 : ")
    if userChoice == "X":
        cpuChoice = "0"
    else:
        cpuChoice = "X"

    game = True
    while game:
        if userMove(userChoice) == "winner":
            print("User win...")
            break
        gameBoard()

        if cpuMove(cpuChoice) == "winner":
            print("CPU Win...")
            break
        gameBoard()

    gameBoard()

main()
